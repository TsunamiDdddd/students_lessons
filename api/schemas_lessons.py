import re
import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import validator

class ShowLesson(BaseModel):
    lesson_id: int
    title: str
    description: str
    content: str
    class Config:
        orm_mode= True

class LessonCreate(BaseModel):
    lesson_id: int
    title: str
    description: str
    content: str
    class Config:
        orm_mode= True

class UpdateLessonRequest(BaseModel):
    title: Optional[constr(min_length=1)]
    description: Optional[constr(min_length=1)]
    content: Optional[constr(min_length=1)]

