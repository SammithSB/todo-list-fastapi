from pydantic import BaseModel

class Task(BaseModel):
    description: str
    complete: bool

