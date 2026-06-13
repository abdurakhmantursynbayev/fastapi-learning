from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from datetime import date


app = FastAPI()

#1-practice task
class User(BaseModel):
    name: str | None = None
    age: int | None = None
    city: str | None = None

users = {
    1: {
        "name": "Jhon",
        "age": 20,
        "city": "london"
    }
}

@app.patch("/users/{user_id}")
async def update_user(user_id: int, user: User) -> User:
    data_from_bd = users[user_id]
    data_from_bd_model = User(**data_from_bd)
    new_data = user.model_dump(exclude_unset=True)
    updated_data = data_from_bd_model.model_copy(update=new_data)
    users[user_id] = jsonable_encoder(updated_data)
    print(users)
    return updated_data

#2-practice task

class Profile(BaseModel):
    username: str | None = None
    bio: str | None = None
    age: int | None = None
    country: str | None = None

profiles = {
    1: {
        "username": "abdurakhman",
        "bio": "I love python and money",
        "age": 18,
        "country": "Kazakhstan"
    }
}

@app.patch("/profiles/{profile_id}")
async def update_profile(profile_id: int, profile: Profile):
    data_from_bd = profiles[profile_id]
    new_data = profile.model_dump(exclude_unset=True)
    data_from_bd_model = Profile(**data_from_bd)
    updated_data = data_from_bd_model.model_copy(update = new_data)
    profiles[profile_id] = jsonable_encoder(updated_data)
    return updated_data

#3-practice task

class Book(BaseModel):
    name: str | None = None
    author: str | None = None
    published: date | None = None
    genre: str | None = None
    pages: int | None = None

books = {
    1: {
        "name": "Atomic Habits",
        "author": "James Clear",
        "published": "2018-10-16",
        "genre": "Self-help",
        "pages": 320
    },
    2: {
        "name": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "published": "1937-09-21",
        "genre": "Fantasy",
        "pages": 310
    }
}

@app.patch("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    if book_id not in books.keys():
        raise HTTPException(status_code=404, detail="book not found")
    data_from_bd = books[book_id]
    data_from_bd_model = Book(**data_from_bd)
    new_data = book.model_dump(exclude_unset=True)
    updated_data = data_from_bd_model.model_copy(update=new_data)
    books[book_id] = jsonable_encoder(updated_data)
    return updated_data