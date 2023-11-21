import uvicorn
from fastapi import FastAPI

from auth.auth import auth_backend, fastapi_users
from endpoints.endpoints import router
from schemas.schemas import UserRead, UserCreate


app = FastAPI(
    title="Notes App"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
