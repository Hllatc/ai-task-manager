from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate
from app.models.task import Task

def create_task(db: Session, task: TaskCreate, user_id: int):
    db_task = Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task(db: Session, task_id: int, user_id: int):
    return db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

def update_task(db: Session, task_id: int, task: TaskCreate, user_id: int):
    db_task = get_task(db, task_id, user_id)

    if db_task:
        db_task.title = task.title
        db_task.description = task.description

        db.commit()
        db.refresh(db_task)

    return db_task

def delete_task(db: Session, task_id: int, user_id: int):
    db_task = get_task(db, task_id, user_id)

    if db_task:
        db.delete(db_task)
        db.commit()

    return db_task