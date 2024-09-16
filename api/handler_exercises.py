from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from api.actions.exercise import _create_new_exercise
from api.actions.exercise import _update_exercise
from api.actions.exercise import _get_exercise_by_id
from api.schemas_exercises import ShowExercise
from api.schemas_exercises import ExerciseCreate
from db.session import get_db
from logging import getLogger

logger = getLogger(__name__)

exercise_router = APIRouter()


@exercise_router.post("/",response_model=ShowExercise)
async def create_exercise(
        body: ExerciseCreate,db: AsyncSession = Depends(get_db))-> ShowExercise:
    try:
        return await _create_new_exercise(body,db)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Ошибка бд: {err}")


@exercise_router.get("/",response_model=ShowExercise)
async def get_exercise_by_id(exercise_id:int,db: AsyncSession = Depends(get_db))-> ShowExercise:
    exercise = await _get_exercise_by_id(
        exercise_id,
        db
    )
    if exercise is None:
        raise HTTPException(
            status_code=404, detail=f"Урок с id {exercise_id} не найден."
        )
    return exercise

@exercise_router.get("/",response_model=ShowExercise)
async def get_exercises_by_lesson_id(lesson_id: int,db: AsyncSession = Depends(get_db)) -> ShowExercise:




