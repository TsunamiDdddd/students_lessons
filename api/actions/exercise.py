from db.models import Exercise
from api.schemas_exercises import ShowExercise,ExerciseCreate
from db.exercise_dals import ExerciseDAL


async def _create_new_exercise (body: ExerciseCreate, session) -> ShowExercise:
    async with session.begin():
        exercise_dal = ExerciseDAL(session)
        exercise = await exercise_dal.create_exercise(
            exercise_id=body.exercise_id,
            lesson_id=body.lesson_id,
            title=body.title,
            description= body.description,
            type = body.type,
            questions=body.questions
        )
        return ShowExercise(
            exercise_id = exercise.exercise_id,
            lesson_id = exercise.lesson_id,
            title = exercise.title,
            description = exercise.description,
            type=exercise.type,
            questions=exercise.questions
        )


async def _update_exercise(
        updated_exercise_params: dict, exercise_id: int, session
)-> int | None:
    async with session.begin():
        exercise_dal = ExerciseDAL(session)
        updated_exercise_id = await exercise_dal.update_exercise(
            exercise_id=exercise_id,**updated_exercise_params
        )
        return updated_exercise_id


async def _get_exercise_by_id(exercise_id, session) -> Exercise | None:
    async with session.begin():
        exercise_dal = ExerciseDAL(session)
        exercise = await exercise_dal.get_exercise_by_id(
            exercise_id=exercise_id
        )
        if exercise is not None:
            return exercise

async def _get_exercises_by_lesson_id(lesson_id, session) -> list | None:
    async with session.begin():
        exercise_dal = ExerciseDAL(session)
        exercises = await exercise_dal.get_exercises_by_lesson_id(
            lesson_id=lesson_id
        )
        if exercises is not None:
            return exercises

