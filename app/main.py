from fastapi import FastAPI
from app.database import engine, Base
from app.models.user import User
from app.models.task import Task 

from app.routers.auth import router as auth_router
from app.routers.task_router import router as task_router
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from app.database import get_db
from app.dependencies.auth import get_current_user


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router,prefix="/auth",tags=["Auth"])
app.include_router(task_router, prefix="/tasks", tags=["Tasks"])

@app.get("/")
def root():
    return {
        "message": "AI Task Manager API"
    }
