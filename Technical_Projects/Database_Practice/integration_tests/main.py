from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    name: str
    completed: bool

# Mock Database
todos = {}

@app.get("/", response_model=List[Todo])
async def read_todos():
    return list(todos.values())

@app.post("/", response_model=Todo)
async def create_todo(todo: Todo):
    todo_id = str(len(todos) + 1)  # use len(todos), not len(todo)
    todos[todo_id] = todo
    return todo

@app.get("/{todo_id}", response_model=Todo)
async def read_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, updated_todo: Todo):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[todo_id] = updated_todo
    return updated_todo

@app.delete("/{todo_id}", response_model=Todo)
async def delete_todo(todo_id: str):
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return todo