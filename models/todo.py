from datetime import datetime
from typing import Union
from pydantic import UUID4, BaseModel


class Todo(BaseModel):
    id: int
    user_id: UUID4
    description: str
    is_completed: bool
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
