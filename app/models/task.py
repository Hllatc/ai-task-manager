# models.py
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from app.database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")