from logging import getLogger
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from api.actions.lesson import _create_new_lesson
from api.actions.lesson import _update_lesson
from api.actions.lesson import _get_lesson_by_id
from db.lesson_dals import LessonDAL
from api.schemas_lessons import ShowLesson
from api.schemas_lessons import LessonCreate
from api.schemas_lessons import UpdateLessonRequest
from api.schemas_lessons import UpdateLessonResponse
from db.session import get_db

logger = getLogger(__name__)

lesson_router = APIRouter()


@lesson_router.post("/", response_model=ShowLesson)
async def create_lesson(body: LessonCreate, db:AsyncSession = Depends(get_db))-> ShowLesson:
    try:
        return await _create_new_lesson(body,db)
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Ошибка бд: {err}")


@lesson_router.get("/",response_model=ShowLesson)
async def get_lesson_by_id(lesson_id: int, db: AsyncSession = Depends(get_db))-> ShowLesson:
    lesson = await _get_lesson_by_id(lesson_id,db)
    if lesson is None:
        raise HTTPException(
            status_code=404, detail=f"Урок с id {lesson_id} не найден."
        )
    return lesson


@lesson_router.patch("/",response_model= UpdateLessonResponse)
async def update_lesson_by_id(
    lesson_id: int,
    body: UpdateLessonRequest,
    db:AsyncSession = Depends(get_db)
)-> UpdateLessonResponse:
    updated_lesson_params = body.dict(exclude_none = True)
    if updated_lesson_params == {}:
        raise HTTPException(
            status_code=422,
            detail="Ни один параметр не передан.",
        )
    user_for_update = await _get_lesson_by_id(lesson_id, db)
    if user_for_update is None:
        raise HTTPException(
            status_code=404, detail=f"Урок с id {lesson_id} не найден."
        )
    try:
        updated_lesson_id = await _update_lesson(
            updated_lesson_params=updated_lesson_params, session=db, lesson_id=lesson_id
        )
    except IntegrityError as err:
        logger.error(err)
        raise HTTPException(status_code=503, detail=f"Ошибка БД: {err}")
    return UpdateLessonResponse(updated_lesson_id=updated_lesson_id)
