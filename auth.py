from typing import Annotated
from fastapi import HTTPException, Header
import jwt

from config import Settings
from models.user import User

settings = Settings()


async def validate_jwt(authorization: Annotated[str, Header()]) -> User:
    jwt_token = authorization.split(" ")[1]

    try:
        if jwt_token is not None:
            decoded = jwt.decode(
                jwt_token,
                settings.supabase_jwt_secret,
                algorithms=["HS256"],
                options={"verify_aud": False, "verify_signature": True},
            )
        else:
            raise HTTPException(status_code=400, detail="Invalid Authorization")

    except jwt.InvalidSignatureError as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=400, detail="Invalid Authorization")
    else:
        user = User(user_id=decoded["sub"], email=decoded["email"])
        return user
