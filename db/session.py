from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

import settings

# Для взаимодействия с БД

# Создание движка для соединения с БД асинхронно
engine = create_async_engine(
    settings.REAL_DATABASE_URL,
    future=True,
    echo=True,
    execution_options={"isolation_level": "AUTOCOMMIT"},
)

# Создание сессии соединения с БД
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> Generator:
    """Получение асинхронной сессии соединения с БД"""
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()
