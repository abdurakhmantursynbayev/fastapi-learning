from enum import Enum
from fastapi import FastAPI

class GameName(str, Enum):
    minecraft = "minecraft"
    cs2 = "cs2"
    dota2 = "dota2"


app = FastAPI()

@app.get("/users/me")
async def current_user():
    return {"user": "current user"}

@app.get("/users/{user_id}")
async def get_user_id(user_id: int):
    return {"user_id": user_id}

@app.get("/games/{game_name}")
async def games(game_name: GameName):
    if game_name is GameName.minecraft:
        return {
            "game": game_name,
            "genre": "sandbox"
        }
    elif game_name.value == "cs2":
        return {
            "game": game_name,
            "genre": "shooter"
        }
    else:
        return {
            "game": game_name,
            "genre": "moba"
        }
