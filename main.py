"""
Minimal FastAPI CRUD example used in the notebooks.

Quickstart:
    uvicorn main:app --reload
    # then open http://127.0.0.1:8000/docs for interactive docs
"""
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Task(BaseModel):
    """Shape of a task resource that flows through requests and responses."""

    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


app = FastAPI(title="FastAPI CRUD Demo")

# Simple in-memory store; replace with a real DB in production
tasks_db: List[Task] = []


# ---- Public endpoints ----

@app.get("/")
def read_root() -> dict:
    # Lightweight health/info route
    return {"message": "API is running"}


@app.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: Task) -> Task:
    """Create a task; we auto-assign an incrementing ID."""
    # Use current length as a naïve auto-increment; collisions reset when process restarts.
    task.id = len(tasks_db) + 1
    tasks_db.append(task)
    return task


@app.get("/tasks/", response_model=List[Task])
def read_tasks() -> List[Task]:
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int) -> Task:
    """Fetch one task or raise a 404 if it is missing."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task) -> Task:
    """Replace all fields of a task; ID stays stable."""
    # Overwrites the whole record; partial updates would use PATCH with a different schema.
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task.id = task_id
            tasks_db[i] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int) -> None:
    """Delete a task; return 204 No Content on success."""
    for i, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")


@app.get("/search/", response_model=List[Task])
def search_tasks(keyword: Optional[str] = None) -> List[Task]:
    # Case-insensitive substring match across task titles; returns all tasks when no keyword is provided.
    if keyword:
        return [task for task in tasks_db if keyword.lower() in task.title.lower()]
    return tasks_db


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
