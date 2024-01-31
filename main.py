from typing import List
from typing_extensions import Annotated

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from supabase import Client

from libs.supabase import get_supabase_client
from auth import validate_jwt
from models.todo import Todo


origins = [
    "http://127.0.0.1:3000",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", dependencies=[Depends(validate_jwt)])
async def home():
    return {"msg": "Hello World!"}


@app.get("/todos")
async def get_todos(
    supabase: Annotated[Client, Depends(get_supabase_client)]
) -> List[Todo]:
    todos = supabase.table("todos").select("*").execute()

    return [Todo(**item) for item in todos.data]
