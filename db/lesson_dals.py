from typing import Union
from uuid import UUID

from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Lesson

class LessonDAL:
    def __init__(self,db_session: AsyncSession):
        self.db_session = db_session

    async def create_lesson(
            self,
            lesson_id: int,
            title: str,
            description: str,
            content: str

    ) -> Lesson:
        new_lesson = Lesson(
            lesson_id=lesson_id,
            title=title,
            description=description,
            content=content
        )
        self.db_session.add(new_lesson)
        await self.db_session.flush()
        return new_lesson
    async def get_lesson_by_id(self,lesson_id:int)-> Union[Lesson,None]:
        query = select(Lesson).where(Lesson.lesson_id == lesson_id)
        res = await self.db_session.execute(query)
        lesson_row = res.fetchone()
        if lesson_row is not None:
            return lesson_row[0]

    async def update_lesson(self, lesson_id: int,**kwargs)->Union[Lesson,None]:
        query = ()