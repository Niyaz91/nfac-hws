from fastapi import FastAPI, HTTPException
import asyncio
from typing import List
from Data_bases.repositories_sql.sql_repository import SQLRepository

app  = FastAPI()
student_repo = SQLRepository("students")  # Для студентов
teacher_repo = SQLRepository("teachers")

class Student ():
    category: str
    name: str
    gpa: float
    study_year: int

class Teacher():
    category: str
    name: str
    subject: str
    years_of_experience: int

@app.get("/students", response_model=List[dict])
async def get_students():
    students = await student_repo.read(record_id=None, category="Student",name=None,gpa=None,study_year=None)
    return students

@app.get("/students/{student_id}", response_model=dict)
async def get_student(student_id: int):
    student = await student_repo.get_connection().fetchrow(f"SELECT * FROM students WHERE  = {student_id}")
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/students/{student_id}", response_model=dict)
async def get_student(student_id: int):
    student = await student_repo.read(record_id=student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student[0]

@app.get("/teachers/", response_model=dict)
async def get_teachers():
    teachers = await teacher_repo.read()
    return teachers

@app.get("/teachers/{teacher_id}", response_model=dict)
async def get_teacher(teacher_id: int):
    teacher = await teacher_repo.read(record_id=teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher[0]


