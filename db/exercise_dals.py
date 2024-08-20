from typing import Union


from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.dialects.postgresql import json
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Exercise

class Question:
    id: int
    question: str
    answer: str
    completed: bool
class ExerciseDAL:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_exercise(
            self,
            exercise_id: int,
            lesson_id: int,
            title: str,
            description: str,
            type: str,
            questions: json
    ) -> Exercise:
        new_exercise = Exercise(
            exercise_id = exercise_id,
            lesson_id = lesson_id,
            title = title,
            description = description,
            type = type,
            questions = questions
        )
        self.db_session.add(new_exercise)
        await self.db_session.flush()
        return new_exercise

    async def get_exercise_by_id(self, exercise_id:int) -> Union[Exercise,None]:
        query = select(Exercise).where(Exercise.exercise_id == exercise_id)
        res = await self.db_session.execute(query)
        exercise_row = res.fetchone()
        if exercise_row is not None:
            return exercise_row[0]

    async def update_exercise(self,exercise_id:int,**kwargs) -> Union[Exercise,None]:
        query = (
            update(Exercise)
            .where(Exercise.exercise_id == exercise_id)
            .values(kwargs)
            .returning(Exercise.exercise_id)
        )
        res=await self.db_session.execute(query)
        update_exercise_id_row = res.fetchone()
        if update_exercise_id_row is not None:
            return update_exercise_id_row[0]
        