# Dependencies with YIELD

from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated, Any


app = FastAPI()

#1-practice task

def get_connection():
    connect_file = open("text", "r")
    try:
        yield connect_file
    finally:
        connect_file.close()

@app.get("/users")
async def read_user(file: Annotated[Any, Depends(get_connection)]):
    text = file.readline()
    text = text[:-1]
    return text

#2-practice task

def get_university():
    try:
        yield "SITE"
    finally:
        print("типо закрылся какое то соединения")

def get_faculty(faculty: Annotated[str, Depends(get_university)]):
    try:
        yield "abdu, Jhon, Michael"
    finally:
        print("типо закрылся тоже хз")

def get_student(student: Annotated[str, Depends(get_faculty)]):
    try: 
        yield "yes, yes, no"
    finally:
        print("типо закрылся тоже")
def exam_access(params: Annotated[str, Depends(get_student)]):
    try:
        yield "information about students"
    finally:
        print("типо закрылся")
    

@app.get("/students")
async def read_user(students: Annotated[str, Depends(exam_access)]):
    return {
        "message": students
    }

#3-practice task

class ExamError(Exception):
    pass

def get_exam_permission():
    try:
        yield {"student_status": "accepted"}
    except ExamError:
        print("error")
        raise
    finally:
        print("connection прервано")

@app.get("/exam")
async def read_exam(permission: Annotated[dict, Depends(get_exam_permission)]):
    if permission["student_status"] == "blocked":
        raise ExamError()
    
    return "nothing"

