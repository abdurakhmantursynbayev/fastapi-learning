from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr
from decimal import Decimal
from uuid import UUID
from typing import Annotated

#1
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr


app = FastAPI()
@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    #тут будет создать user в бд а потом после создания берем его id  например id=0
    return {
        "id":0,
        **user.model_dump()
    }

#2
class PlayerPublic(BaseModel):
    id: int
    nickname: str

class PlayerInDB(BaseModel):
    id: int
    nickname: str
    email: EmailStr
    steam_balance: Decimal
    is_admin: bool | None = False


@app.get("/players/{player_id}", response_model=PlayerPublic)
async def get_player(player_id: int):
    #тут через id надо было взять данные из бд потом превратить его на playerindb потом вернуть его 
    data = PlayerInDB(id= player_id, nickname="abdu",email= 'abdu@gmail.com', steam_balance= 10000, is_admin= False)
    return data

#3

class BaseGame(BaseModel):
    title: str
    genre: str
    price: float

class GameCreate(BaseGame):
    secret_developer_note: str

@app.post("/games/")
async def create_game(game: GameCreate) -> BaseGame:
    return game

#4
class MovieResponse(BaseModel):
    id: int
    title: str
    rating: str

data_movies = [
    {
        "id": 1,
        "title": "The Dark Knight",
        "rating": "9.0",
        "genre": "Action",
        "year": "2008-07-18"
    },
    {
        "id": 2,
        "title": "Interstellar",
        "rating": "8.7",
        "genre": "Sci-Fi",
        "year": "2014-11-07"
    },
    {
        "id": 3,
        "title": "The Shawshank Redemption",
        "rating": "9.3",
        "genre": "Drama",
        "year": "1994-09-23"
    },
    {
        "id": 4,
        "title": "Inception",
        "rating": "8.8",
        "genre": "Sci-Fi",
        "year": "2010-07-16"
    },
    {
        "id": 5,
        "title": "Fight Club",
        "rating": "8.8",
        "genre": "Drama",
        "year": "1999-10-15"
    }
]

@app.get("/movies/", response_model=list[MovieResponse])
async def get_movies(id_movies: Annotated[list[int], Query()]):
    #кароче тут будет запрос в бд и оттуда берем типо топ фильмы не меньше пяти 
    data_response_m = []
    for i in id_movies:
        data_response_m.append(data_movies[i])
    return data_response_m


#5
data_students = [
    {
        "name": "Abdurakhman",
        "email": "abdurakhman@gmail.com",
        "github": "https://github.com/abdurakhman",
        "linkedin": "https://linkedin.com/in/abdurakhman"
    },
    {
        "name": "Aruzhan",
        "email": "aruzhan@gmail.com",
        "github": "https://github.com/aruzhan",
        "linkedin": "https://linkedin.com/in/aruzhan"
    },
    {
        "name": "Nursultan",
        "email": None,
        "github": None,
        "linkedin": "https://linkedin.com/in/nursultan"
    }
]
class StudentResponse(BaseModel):
    name: str
    email:EmailStr | None = None
    github: str | None = None
    linkedin: str

@app.get("/users/user/{user_id}", response_model= StudentResponse, response_model_exclude_none=True)
async def create_student(user_id: int):
    return data_students[user_id]

#6

class Laptop(BaseModel):
    name: str
    ram: str | None = "8GB"
    gpu: str
    cpu: str
    battery: str | None = "100%"

laptops = [
    {
        "name": "Lenovo Legion 5",
        "gpu": "RTX 4060",
        "cpu": "Ryzen 7 7840HS",
        "battery": "92%"
    },
    {
        "name": "ASUS TUF A15",
        "gpu": "RTX 4070",
        "cpu": "Ryzen 9 7940HS",
    },
    {
        "name": "MacBook Air M3",
        "ram": "16GB",
        "gpu": "Apple M3 GPU",
        "cpu": "Apple M3",
        "battery": "100%"
    }
]

@app.get("/laptops/{laptop_id}", response_model=Laptop, response_model_exclude_unset=True)
async def about_laptop(laptop_id: int):
    return laptops[laptop_id]
