from datetime import date
from typing import List, Union
from fastapi import FastAPI, Depends
from pydantic import UUID4, BaseModel
from typing_extensions import Annotated
from supabase import Client

from libs.supabase import get_supabase_client
from models.todo import Todo


app = FastAPI()


@app.get("/todos")
async def get_todos(
    supabase: Annotated[Client, Depends(get_supabase_client)]
) -> List[Todo]:
    todos = supabase.table("todos").select("*").execute()

    return [Todo(**item) for item in todos.data]


@app.get("/todos/{id}")
async def get_todo_by_id(
    id: int, supabase: Annotated[Client, Depends(get_supabase_client)]
) -> Todo:
    todo = supabase.table("todos").select("*").eq("id", id).single().execute()
    print(todo)
    return Todo(**todo.data)


@app.post("/")
async def create_todo(todo: Todo):
    return {todo}
