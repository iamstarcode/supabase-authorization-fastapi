from typing import Annotated
from fastapi import HTTPException, Header
import jwt

from config import Settings

settings = Settings()


def validate_jwt(authorization: Annotated[str, Header()]) -> str:
    access_token = authorization.split(" ")[1]

    try:
        if access_token is not None:
            decoded = jwt.decode(
                access_token,
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
        return access_token
