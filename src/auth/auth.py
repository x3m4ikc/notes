from fastapi_users import FastAPIUsers
from fastapi_users.authentication import BearerTransport
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend

from auth.manager import get_user_manager
from config import SECRET_KEY
from models.models import User

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


