import re
import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel, Json
from pydantic import constr
from pydantic import EmailStr
from pydantic import validator


class ShowExercise(BaseModel):
    exercise_id: int
    lesson_id: int
    title: str
    description: str
    type: str
    questions: Json

    class Config:
        orm_mode = True


class ExerciseCreate (BaseModel):
    exercise_id: int
    lesson_id: int
    title: str
    description: str
    type: str
    questions: Json

    class Config:
        orm_mode = True
