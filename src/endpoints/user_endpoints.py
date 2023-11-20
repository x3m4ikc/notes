from fastapi import APIRouter, status, HTTPException
from schemas.schemas import UserSchema
from services.crud import create_new_user, get_user
from services.help_functions import generate_access_token, make_hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", name="register", status_code=status.HTTP_201_CREATED)
async def register(data: UserSchema):
    hashed_password = make_hash_password(data.password)
    try:
        new_user = await create_new_user(data.login, hashed_password)
        return {"id": new_user.id, "login": new_user.username}
    except BaseException:
        raise HTTPException(status_code=400, detail="This username is occupied")


@router.post("/token", name="token", status_code=status.HTTP_200_OK)
async def login_for_access_token(data: UserSchema):
    try:
        user = await get_user(data.login)
        if user and make_hash_password(data.password) == user.hashed_password:
            access_token = generate_access_token(user)
            return {"access_token": access_token, "token_type": "bearer"}
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
