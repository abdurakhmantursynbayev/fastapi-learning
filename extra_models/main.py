from fastapi import FastAPI, Query
from pydantic import BaseModel, EmailStr
from typing import  Union, Annotated
from decimal import Decimal
from datetime import date, timedelta

app = FastAPI()

#1-practice task
class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublic(BaseModel):
    id: int
    username: str

class UserInDB(UserPublic):
    email: EmailStr
    hashed_password: str

def fake_password_hashed(password: str):
    hashed_password = "notsupersecurity" + password
    return hashed_password

def save_fake_password_with_info(user: UserRegister):
    hashed_passwordd = fake_password_hashed(user.password)
    # тут мы крч добавляем на бд и тогда бд нам вернет ID того и будем сохронить но пока что id = 0
    data_in_db = UserInDB(**user.model_dump(), id = 0, hashed_password=hashed_passwordd)
    return data_in_db

@app.post("/users/", response_model = UserPublic)
async def create_user(user: UserRegister):
    data_response = save_fake_password_with_info(user)
    return data_response

#2-practice task

class BaseItem(BaseModel):
    name: str
    rarity: str

class WeaponItem(BaseItem):
    damage: int

class ArmorItem(BaseItem):
    defense: str

@app.get("/inventory/{item_id}", response_model= Union[WeaponItem, ArmorItem])
async def get_item(item_id: int):
    #тут будет запрос на бд используя id
    return {
        "name": "ak-47",
        "rarity": "strong",
        "damage": 10
    }

#3-practice task

class GameBase(BaseModel):
    title: str
    price: Decimal

class GameCreate(GameBase):
    developer_note: str

@app.post("/games/", response_model=GameBase)
async def create_game(game: GameCreate):
    return game

#4-practice task

class MovieBase(BaseModel):
    title: str
    year: date

class MovieInDB(MovieBase):
    internal_rating: float
    revenue: Decimal

class MoviePublic(MovieBase):
    pass 

@app.get("/movies/{movie_id}", response_model=MoviePublic)
async def get_movie(movie_id: int):
    #тут будет запрос на дб используя id
    data_from_db = MovieInDB(title= "hello", year=date(year=2020, month=10, day=5), internal_rating=9.5, revenue=1000000)
    return data_from_db

#5-practice task

class TextMessage(BaseModel):
    content: str
    type: str = "text"

class ImageMessage(BaseModel):
    image_url: str
    type: str = "image"

class VoiceMessage(BaseModel):
    audio_url: str
    duration: timedelta
    type: str = "voice"

@app.get("/message/{message_id}", response_model= VoiceMessage | TextMessage | ImageMessage)
async def get_message(message_id: int):
    #тут можно было бы отправить запрос на бд что бы узнать какой тип ответа нам вернуть
    return {
        "audio_url": "https//:aaa",
        "duration": timedelta(minutes=2)
    }

#6 practice task

@app.get("/messages", response_model= list[TextMessage | ImageMessage | VoiceMessage])
async def get_messages(messages_id: Annotated[list[int], Query()]):
    #тут будет сделать запрос из list of ids потом их сохроняем в лист и вернем
    return [
    {
        "content": "Hello, how are you?",
        "type": "text"
    },
    {
        "image_url": "https://example.com/cat.jpg",
        "type": "image"
    },
    {
        "audio_url": "https://example.com/voice.mp3",
        "duration": "00:01:30",
        "type": "voice"
    },
    {
        "content": "This is another text message",
        "type": "text"
    },
    {
        "image_url": "https://example.com/sunset.jpg",
        "type": "image"
    }
    ]

