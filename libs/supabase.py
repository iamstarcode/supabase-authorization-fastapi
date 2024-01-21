from typing import Annotated
from fastapi import Depends, Header
from supabase.client import Client, ClientOptions
from auth import validate_jwt
from models.user import User

from config import Settings

settings = Settings()


async def get_supabase_client(
    authorization: Annotated[str, Header()],
    user: Annotated[User, Depends(validate_jwt)],
) -> Client:
    access_token = authorization.split(" ")[1]
    supabase = Client(
        settings.supabase_url,
        settings.supabase_key,
        options=ClientOptions(
            persist_session=False,
            auto_refresh_token=False,
            headers=({"Authorization": f"Bearer {access_token}c"}),
        ),
    )

    # supabase.auth.set_session(access_token, refresh_token="")
    return supabase
