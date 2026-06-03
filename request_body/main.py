from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

class Game(BaseModel):
    title: str
    price: float
    genre: str


class Platform(str, Enum):
    pc = "pc"
    playstation = "playstation"
    xbox = "xbox"

class Review(BaseModel):
    author: str
    rating: int
    comment: str

app = FastAPI()

@app.post("/games/")
async def creating_game(game: Game):
    game_dict = game.model_dump()
    price_with_tax = game_dict.pop("price") * 1.12
    game_dict["price_with_tax"] = price_with_tax
    return {
        "message": "game created",
        "game": game_dict
    }

@app.get("/games/{game_id}")
async def game_lang(game_id: int, lang: str | None = None):
    result = {"game_id": game_id}
    if lang:
        result.update({"lang": lang})
    return result

@app.get("/platform/{platform}")
async def about_platform(platform: Platform):
    if platform is Platform.pc:
        return {
            "message": "good choice, pc is the best"
        }
    elif platform.value == "xbox":
        return {
            "message": "oooo good, xbox is my favourite "
        }
    else:
        return {
            "message": "ps5 is the best"
        }
    
@app.post("/games/{game_id}/review/")
async def review_info_about_g(game_id: int, review: Review):
    return {
        "game_id": game_id,
        "review": review
    }
