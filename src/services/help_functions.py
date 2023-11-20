import datetime
from jose import JWTError, jwt
import hashlib
import binascii
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def generate_access_token(user):
    expire_in = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"id": user.id, "exp": expire_in}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token


def make_hash_password(password, iterations=100_000):
    dk = hashlib.pbkdf2_hmac(
        password=password.encode("utf-8"),
        salt=SECRET_KEY.encode("utf-8"),
        iterations=iterations,
        hash_name=ALGORITHM,)
    return binascii.hexlify(dk).decode("ascii")
