from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import students, courses, grades

app = FastAPI(title="Smart Student Management System")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(grades.router, prefix="/grades", tags=["Grades"])
