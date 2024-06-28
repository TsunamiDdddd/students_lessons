import uuid
from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
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
class Lesson(Base):
    __tablename__="lessons"
    lesson_id = Column(Integer, primary_key = True)
    title = Column(VARCHAR,nullable = True)
    description = Column(Text,nullable = True)
    content = Column(Text,nullable = True)



