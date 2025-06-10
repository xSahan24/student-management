from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import Student

router = APIRouter()

@router.post("/")
def create_student(student: Student, session: Session = Depends(get_session)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

@router.get("/")
def read_students(session: Session = Depends(get_session)):
    return session.exec(select(Student)).all()
