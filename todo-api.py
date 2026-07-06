from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    name: str
    title: str
    completed: bool

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"todo list": todos}

@app.get("/todos")
def read_todos():
    return {"todos": todos}

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todos": todo}
    return "not found"

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"todos": todos[index]}
    return "id not found"

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            # todos.remove(todos[index])
            todos.pop(index)
            return {"removed"}
    return "not found"