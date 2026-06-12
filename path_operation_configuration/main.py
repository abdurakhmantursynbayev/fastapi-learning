from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


#1-practice task
class Book(BaseModel):
    name: str
    author: str
    rating: str | None = None

@app.post("/books", status_code=201)
async def create_book(book: Book):
    return {"book": book}

#2-practice task

class Tags(Enum):
    books = "books"
    authors = "authors"

@app.get("/users/user/{user_id}", tags=[Tags.books])
async def read_user(user_id: int):
    return {"user_id": user_id}

@app.post("/books/book", tags=[Tags.books])
async def create_book(book: Book):
    return {"book": book}

@app.get("/authors/{author_name}", tags=[Tags.authors])
async def read_author(author_name: str):
    return {
        "author": author_name
    }

#3-practice task
class Movie(BaseModel):
    name: str
    country: str

@app.post("/movies/movie", summary="created movie", description="""
Create a movie.
          
Store movie information.
          
Return created movie.

""")
async def create_movie(movie: Movie):
    return {
        "movie": movie
    }

#4-practice task


class Student(BaseModel):
    name: str
    age: int
    group: str

@app.post("/students/student", summary="creating student in db")
async def create_student(student: Student):
    """
    ## features
    

    - **name**

    - **age**

    - **group**
    """
    return {
        "student": student
    }

#5-6-7 practice tasks

class Product(BaseModel):
    id: int
    name: str
    type: str

@app.post("/products/product", tags=["Product"], summary="creating product in db", status_code=201, response_description="product with features  -id, -name, -type", deprecated=True)
async def create_product(product: Product):
    """
    ## product information

    - **id**
    
    - **name**

    - **type**
    """
    return {
        "product": product
    }