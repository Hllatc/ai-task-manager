from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.schemas.task import TaskCreate
from app.models.user import User
from app import crud

router = APIRouter()

@router.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud.create_task(db, task, user.id)

@router.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud.get_tasks(db, user.id)

@router.get("/tasks/{task_id}")
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud.get_task(db, task_id, user.id)

@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud.update_task(db, task_id, task, user.id)

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return crud.delete_task(db, task_id, user.id)