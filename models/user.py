from pydantic import UUID4, BaseModel


class User(BaseModel):
    user_id: UUID4
    email: str


class UserWithAccessToken(User):
    access_token: str
