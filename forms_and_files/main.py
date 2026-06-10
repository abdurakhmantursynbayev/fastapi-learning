from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel, EmailStr
from typing import Annotated
from decimal import Decimal

#1- practice task
class PlayerRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

app = FastAPI()
@app.post("/register/")
async def register_player(player: Annotated[PlayerRegister, Form()]):
    return {
        "player": player
    }

#2-practice task
class BookCreate(BaseModel):
    title: str
    author: str
    price: Decimal

@app.post("/books")
async def create_book(book: Annotated[BookCreate, Form()]):
    return {
        "book": book
    }

#3-practice task
@app.post("/avatar")
async def create_movie(file: UploadFile):
    return {
        "filename": file.filename,
        "content-type": file.content_type
    }

#4-practice task
@app.post("/document")
async def create_document(file: Annotated[bytes, File()]):
    return {
        "size": len(file)
    }

#5-practice task
@app.post("/screenshots")
async def create_movies(files: list[UploadFile] = File()):
    return {
        "filenames": [i.filename for i in files]
    }


#6-practice task
@app.post("/profile")
async def create_profile(
    username: Annotated[str, Form()],
    bio: Annotated[str, Form()],
    avatar: Annotated[UploadFile, File()]
):
    return {
        "message": "profile created",
        "username": username,
        "bio": bio,
        "avatar_name": avatar.filename
    }

#7-practice task
@app.post("/game-upload")
async def create_games(
    title: Annotated[str, Form()],
    genre: Annotated[str, Form()],
    price: Annotated[Decimal, Form()],
    screenshots: Annotated[list[UploadFile], File()]
):
    return {
        "title": title,
        "screenshots": [i.filename for i in screenshots]
    }

