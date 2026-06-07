from fastapi import FastAPI
from uuid import UUID
from typing import Annotated
from pydantic import BaseModel
from datetime import datetime, date, time,timedelta
from decimal import Decimal


app = FastAPI()

class User(BaseModel):
    id: UUID
    name: str

@app.post("/user/")
async def create_user(user: User):
    return {
        "message": "user created",
        "user": user
    }

class Event(BaseModel):
    name: str
    created_at: datetime

@app.post("/events/")
async def post_event(event: Event):
    return {
        "event": event
    }

class Student(BaseModel):
    name: str
    birthday: date


@app.post("/student/")
async def create_student(student: Student):
    return {
        "student": student
    }

class Movie(BaseModel):
    start_time: time
    name: str
    film_duration: timedelta
    genre: frozenset[str]
    description: bytes
    film_gross: Decimal

@app.post("/movie")
async def create_movie(movie: Movie):
    return {
        "movie": movie
    }