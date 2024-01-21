from typing import Annotated
from fastapi import Depends, Header
from supabase import create_client, Client

from supabase.client import ClientOptions
from auth import validate_jwt
from models.user import User

from config import Settings

settings = Settings()


async def get_supabase_client(
    authorization: Annotated[str, Header()],
    user: Annotated[User, Depends(validate_jwt)],
) -> Client:
    access_token = authorization.split(" ")[1]
    # print(x_refresh_token)
    supabase: Client = create_client(
        settings.supabase_url,
        settings.supabase_anon_key,
        options=ClientOptions(
            persist_session=False,
            auto_refresh_token=False,
            # headers=({"Authorization": f"Bearer {access_token}"}),
        ),
    )

    supabase.auth.set_session(access_token, refresh_token="")
    supabase.postgrest.auth(access_token)

    return supabase
