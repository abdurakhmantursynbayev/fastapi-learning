from fastapi import FastAPI
from enum import Enum

class GameCategory(str, Enum):
    action = "action"
    strategy = "strategy"
    rpg = "rpg"



app = FastAPI()

@app.get("/games/category/{game_cat}")
async def gamecat(game_cat: GameCategory):
    if game_cat is GameCategory.action:
        return {
            "games": ["Hack-and-Slash", "Soulslike", "Battle Royale & Multiplayer"],
            "category": game_cat
        }
    if game_cat.value == "strategy":
        return {
            "games": ["Real-Time Strategy", "Turn-Based Strategy", "Tower Defense"],
            "category": "strategy"
        }
    else:
        return {
            "games": ["black russia", "mobilerp", "gta5"],
            "category": "rpg"
        }
    
@app.get("/games/popular")
async def popular_games():
    return {
        "popular_games": [
            "CS2",
            "Dota 2",
            "Minecraft"
        ]
    }

@app.get("/games/{game_id}")
async def game_info(game_id: int, lang: str | None = None, full_info: bool = False):
    result = {"game_id": game_id}
    if lang:
        result["lang"] = lang
    if full_info:
        result["full_info"] = full_info
    return result


@app.get("/users/{user_id}/games/{game_id}")
async def show_hours(user_id: int, game_id: int, show_hours: bool = False):
    hours = 1 # here will be query from postgresql но пока что они же не связан оставим так
    if show_hours:
        return {
            "user_id": user_id,
            "game_id": game_id,
            "played hours": hours
        }
    return {
        "user_id": user_id,
        "game_id": game_id
    }


@app.get("/search/")
async def searching(q: str | None = None, limit: int = 10):
    #тут тоже должно быть какие то данные из база данных и должно использавать limit 
    return {
        "q": q,
        "limit": limit
    }