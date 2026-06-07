from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    author: str
    title: str
    description: str | None = None
    price: float
    tax: float | None = None
    model_config = {
        'json_schema_extra': {
            'example': 
                {
                    "author": "abdu",
                    "title": "about abdu's life",
                    "description": "aaaaa",
                    "price": 55.5,
                    "tax": 5.5
                }
            
        }
    }

@app.post("/books/")
async def create_book(book: Book):
    return {
        "book": book
    }

class Student(BaseModel):
    name: str
    second_name: str
    specialist: str
    id: int


@app.post("/students")
async def create_student(student: Annotated[Student, Body(openapi_examples= {
                    "normal": {
                        "summary": "a normal example",
                        "value": {
                            "name": "abdu",
                            "second_name": "rakhman",
                            "specialist": "information system",
                            "id": 15
                        }
                    },
                    "invalid": {
                        "summary": "not normal ex",
                        "value": {
                            "name": 5
                        }
                    }
                },),],):
    return {
        "student": student
    }