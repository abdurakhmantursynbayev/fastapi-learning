from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from fastapi.exception_handlers import http_exception_handler


app = FastAPI()


#1-practice task
class UserBlockedException(Exception):
    pass

@app.exception_handler(UserBlockedException)
async def user_blocker_exception(request, exc):
    return JSONResponse(
        status_code=403,
        content={
            "message": "User is blocked"
        }
    )

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id == 13:
        raise UserBlockedException()
    return {
        "user_id": user_id
    }

#2-practice task

@app.exception_handler(StarletteHTTPException)
async def starletteexception_handler(request, exc):
    return PlainTextResponse(content=f"HTTP ERROR: {str(exc.detail)}", status_code=exc.status_code)

@app.get("/players/{player_id}")
async def get_player(player_id: int):
    if player_id > 100:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "player_id": player_id
    }

#3-practice task

@app.exception_handler(RequestValidationError)
async def request_exception_hand(request, exc):
    return PlainTextResponse(content= "Validation failed", status_code=400)

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {
        "item_id": item_id
    }


#4-practice task

@app.exception_handler(RequestValidationError)
async def for_printing_excbody(request, exc):
    print(exc.body)
    return PlainTextResponse(content="Validation failed", status_code=400)

class User(BaseModel):
    name: str
    age: int

@app.post("/users/user")
async def create_user(user: User):
    return {
        "user": user
    }

#5-practice task

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print("HTTP ERROR!")
    return await http_exception_handler(request, exc)

@app.get("/games/{game_id}")
async def get_game(game_id: int):
    if game_id > 15:
        raise HTTPException(status_code=404, detail="game not found")
    return {
        "game_id": game_id
    }