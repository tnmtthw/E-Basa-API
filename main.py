from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import router as user_routes
from routes.question_routes import router as question_routes
from routes.teacher_routes import router as teacher_routes
from routes.instruction_routes import router as instruction_routes
from routes.classroom_routes import router as classroom_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes)
app.include_router(teacher_routes)
app.include_router(question_routes)
app.include_router(instruction_routes)
app.include_router(classroom_routes)