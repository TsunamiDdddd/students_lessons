from db.models import Lesson
from api.schemas_lessons import ShowLesson,LessonCreate,UpdateLessonRequest
from db.lesson_dals import LessonDAL

async def _create_new_lesson (body: LessonCreate, session) -> ShowLesson:
    async with session.begin():
        lesson_dal = LessonDAL(session)
        lesson = await lesson_dal.create_lesson(
            lesson_id= body.lesson_id,
            title=body.title,
            description=body.description,
            content=body.content
        )
        return ShowLesson(
            lesson_id = lesson.lesson_id,
            title=lesson.title,
            description = lesson.description,
            content = lesson.content
        )

async def _update_lesson(
        updated_lesson_params: dict, lesson_id: int, session
) -> int | None:
    async with session.begin():
        lesson_dal = LessonDAL(session)
        updated_lesson_id = await lesson_dal.update_lesson(
            lesson_id=lesson_id, **updated_lesson_params
        )
        return updated_lesson_id

async def _get_lesson_by_id(lesson_id,session) -> Lesson | None:
    async with session.begin():
        lesson_dal = LessonDAL(session)
        lesson = await lesson_dal.get_lesson_by_id(
            lesson_id=lesson_id,
        )
        if lesson is not None:
            return lesson