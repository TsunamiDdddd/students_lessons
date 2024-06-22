import re
import uuid
from typing import Optional

from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import validator

# Модели представлений

LETTER_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")

class ShowUser(BaseModel):
    user_id: uuid.UUID
    name: str
    surname: str
    email: EmailStr
    class Config:
        orm_mode= True


class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    class Config:
        orm_mode= True

    @validator("name")
    def validate_name(cls, value):
        if not LETTER_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="В имени должны быть только буквы"
            )
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="В фамилии должны быть только буквы"
            )
        return value

class DeleteUserResponse(BaseModel):
    deleted_user_id: uuid.UUID
    class Config:
        orm_mode= True

class UpdatedUserResponse(BaseModel):
    updated_user_id: uuid.UUID
    class Config:
        orm_mode= True

class UpdateUserRequest(BaseModel):
    name: Optional[constr(min_length=1)]
    surname: Optional[constr(min_length=1)]
    email: Optional[EmailStr]
    class Config:
        orm_mode= True
    @validator("name")
    def validate_name(cls, value):
        if not LETTER_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="В имени должны быть только буквы"
            )
        return value

    @validator("surname")
    def validate_surname(cls, value):
        if not LETTER_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="В фамилии должны быть только буквы"
            )
        return value


class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        orm_mode= True