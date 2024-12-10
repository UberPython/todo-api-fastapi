from pydantic import BaseModel
from datetime import datetime
from typing import NewType, Optional


# Declare a new type of variable ID
ID = NewType("id", int)


class Task(BaseModel):
    """
    Definition of components of a task
    """

    summary: str
    priority: int
    due_date: Optional[datetime] = None


class TaskList(BaseModel):
    """
    Definition of the TaskList
    """

    id: ID
    task: Task
