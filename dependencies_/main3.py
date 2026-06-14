from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

#1-practice task

class User(BaseModel):
    name: str 
    age: int | None = None
    country: str | None = None

def get_user(user: User):
    if user.country != "Kazakhstan":
        raise HTTPException(status_code=404, detail="User not found!")
    #тут будет запрос на бд и оттуда берем данные
    return {
        "name": "Tom",
        "age": 18,
        "country": "Kazakhstan"
    }

@app.post("/profile/")
async def create_profile(user: Annotated[dict, Depends(get_user)]):
    return {
        "name": user["name"],
        "age": user["age"],
        "country": user["country"]
    }

@app.post("/dashboard", dependencies= [Depends(get_user)])
async def test_profile():
    #тут типо будет проверка если country kazakhstan то будем показывать данные например связанной с казахстан типо сервер для казахов
    #и будем запрос делать в дб и вернуть его 
    return {
        "message": "everything is okay"
    }

#2-practice task

tokens = {"aa", "bb"}  #типо токены админов хаха

def get_token(token: str):
    return token

def verify_token(token: Annotated[str, Depends(get_token)]):
    if token in tokens:
        return token
    raise HTTPException(status_code=404, detail= "token not found")

@app.get("/admin-panel", dependencies=[Depends(verify_token)])
async def check_admin():
    return {
        "message": "Welcome admin!"
    }