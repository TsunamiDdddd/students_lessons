import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from api.handlers import user_router
from api.handler_exercises import exercise_router
from api.handler_lessons import lesson_router
from api.login_handler import login_router

app = FastAPI(title="engl v22")


main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/user", tags=["user"])
main_api_router.include_router(exercise_router, prefix="/exercise", tags=["exercise"])
main_api_router.include_router(lesson_router,prefix="/lesson", tags=["lesson"])
main_api_router.include_router(login_router,prefix="/login",tags=["login"])

app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8010)
