import uuid
from enum import Enum

from sqlalchemy import Boolean, ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy import Text

# Модели данных

Base = declarative_base()


class UserRole(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    SUPERADMIN = "SUPERADMIN"


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=True)
    roles = Column(ARRAY(String), nullable=True)

    @property
    def is_superadmin(self) -> bool:
        return UserRole.SUPERADMIN in self.roles

    @property
    def is_admin(self) -> bool:
        return UserRole.ADMIN in self.roles

    def enrich_admin_roles_by_admin_role(self):
        if not self.is_admin:
            return {*self.roles, UserRole.ADMIN}

    def remove_admin_privileges_from_model(self):
        if self.is_admin:
            return {role for role in self.roles if role != UserRole.ADMIN}


class Lesson(Base):
    __tablename__="lessons"
    lesson_id = Column(Integer, primary_key = True)
    title = Column(VARCHAR,nullable = True)
    description = Column(Text,nullable = True)
    content = Column(Text,nullable = True)


class Exercise(Base):
    __tablename__="exercises"
    exercise_id = Column(Integer,primary_key = True)
    lesson_id = Column(Integer,ForeignKey( "lessons.lesson_id"),nullable=True)
    title = Column(VARCHAR,nullable=True)
    description = Column(Text,nullable=True)
    type = Column(VARCHAR,nullable = True)
    questions = Column(JSON, nullable = True)


class CompletedExercise(Base):
    __tablename__="completed_exercises"
    completed_exercise_id=Column(Integer,primary_key = True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"),nullable = True)
    exercise_id = Column(Integer,ForeignKey("exercises.exercise_id"), nullable = True)
    score = Column(Integer,nullable = True)
    completed_at = Column(TIMESTAMP,nullable=True)
    answers = Column(JSON,nullable=True)


class TypesOfExercises(Base):
    __tablename__="types_of_exercises"
    type_id = Column(Integer,primary_key = True)
    type_title = Column(VARCHAR,nullable = True)
    type_description = Column(Text,nullable=True)