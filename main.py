from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


class Todo(BaseModel):
    name: str
    due_date: str
    description: str


app = FastAPI(title="TODO API")

store_todo = []


@app.get("/")
async def home():
    return {"Hello": "World"}


@app.post("/todo/")
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get("/todo/", response_model=List[Todo])
async def get_all_todos():
    return store_todo


@app.get("/todo/{_id}")
async def get_todo(_id: int):
    try:
        return store_todo[_id]
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.put("/todo/{_id}")
async def update_todo(_id: int, todo: Todo):
    try:
        store_todo[_id] = todo
        return store_todo[_id]
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")


@app.delete("/todo/{_id}")
async def delete_todo(_id: int):
    try:
        obj = store_todo[_id]
        store_todo.pop(_id)
        return obj
    except:
        raise HTTPException(status_code=404, detail="Todo Not Found")
