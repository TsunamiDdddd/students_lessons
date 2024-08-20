from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from api.actions.exercise import _create_new_exercise
from api.actions.exercise import _update_exercise
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
