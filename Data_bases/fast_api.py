from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from typing import List
from Data_bases.repositories_sql.sql_repository import SQLRepository

app  = FastAPI

class Student (BaseModel):
    category: str
    name: str
    gpa: float
    study_year: int


class Teacher(BaseModel):
    category: str
    name: str
    subject: str
    years_of_experience: int

STUDENT_TABLE = "students"
TEACHER_TABLE = "teachers"

async def get_repo(table_name: str):
    return SQLRepository(table_name)

@app.get("/students", response_model=List[dict])
async def get_students():
    repo = await get_repo(STUDENT_TABLE)
    students = await repo.read()
    return students

@app.get("/teachers", response_model=List[dict])
async def get_teachers():
    repo = await get_repo(TEACHER_TABLE)
    teachers = await repo.read()
    return teachers

@app.get("/students/{student_id}", response_model=dict)
async def get_student(student_id: int):
    repo = await get_repo(STUDENT_TABLE)
    student = await repo.read(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.get("/teachers/{teacher_id}", response_model=dict)
async def get_teacher(teacher_id: int):
    repo = await get_repo(TEACHER_TABLE)
    teacher = await repo.read(teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@app.post("/students", response_model=dict)
async def create_student(student: Student):
    repo = await get_repo(STUDENT_TABLE)
    created_student = await repo.create(student.category, student.name, student.gpa, student.study_year)
    return created_student

@app.post("/teachers", response_model=dict)
async def create_teacher(teacher: Teacher):
    repo = await get_repo(TEACHER_TABLE)
    created_teacher = await repo.create(teacher.category, teacher.name, teacher.subject, teacher.years_of_experience)
    return created_teacher

@app.patch("/students/{student_id}", response_model=dict)
async def update_student(student_id: int, student: Student):
    repo = await get_repo(STUDENT_TABLE)
    updated_student = await repo.update(student_id, student.category, student.name, student.gpa, student.study_year)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@app.patch("/teachers/{teacher_id}", response_model=dict)
async def update_teacher(teacher_id: int, teacher: Teacher):
    repo = await get_repo(TEACHER_TABLE)
    updated_teacher = await repo.update(teacher_id, teacher.category, teacher.name, teacher.subject, teacher.years_of_experience)
    if updated_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return updated_teacher

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    repo = await get_repo(STUDENT_TABLE)
    result = await repo.delete(student_id)
    if result:
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/teachers/{teacher_id}")
async def delete_teacher(teacher_id: int):
    repo = await get_repo(TEACHER_TABLE)
    result = await repo.delete(teacher_id)
    if result:
        return {"message": "Teacher deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Teacher not found")

