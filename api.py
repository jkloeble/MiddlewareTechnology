from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import List

app = FastAPI(
    title="API ToDo",
    description="ToDo API.",
    version="0.1",
)

# Dummy list for demonstration purposes
todos = []

#CRUD
@app.get("/health", summary="Health check")
def health():
    """Health check."""
    return JSONResponse(content={"status": "OK"})

@app.post("/save_todo", summary="Create a new ToDo item", response_model=dict)
def save_todo(todo_item: str):
    """Create a new ToDo item."""
    new_todo = {"id": len(todos) + 1, "todo_item": todo_item}
    todos.append(new_todo)
    return new_todo

@app.get("/get_todos", summary="Get all ToDo items", response_model=List[dict])
def get_todos():
    """Get all ToDo items."""
    return todos

@app.get("/get_todo/{todo_id}", summary="Get a ToDo item by ID", response_model=dict)
def get_todo(todo_id: int):
    """Get a ToDo item by ID."""
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return todo

@app.put("/update_todo/{todo_id}", summary="Update a ToDo item by ID", response_model=dict)
def update_todo(todo_id: int, updated_todo: str):
    """Update a ToDo item by ID."""
    todo_index = next((index for index, item in enumerate(todos) if item["id"] == todo_id), None)
    if todo_index is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    todos[todo_index]["todo_item"] = updated_todo
    return todos[todo_index]

@app.delete("/delete_todo/{todo_id}", summary="Delete a ToDo item by ID", response_model=dict)
def delete_todo(todo_id: int):
    """Delete a ToDo item by ID."""
    todo = next((item for item in todos if item["id"] == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    todos.remove(todo)
    return todo
    
