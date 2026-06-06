from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str 

class Review(BaseModel):
    username: str
    rating: int = Field(ge=1, le=10)
    comment: str | None = None

class Publisher(BaseModel):
    name: str
    country: str

class Game(BaseModel):
    title: str
    price: float = Field(gt=0)
    tags: list[str] = Field(default_factory=list)
    images: list[Image] = Field(default_factory=list)
    reviews: list[Review] = Field(default_factory=list)
    publisher: Publisher




@app.post("/games/")
async def game_n(game: Game):
    return {
        "game": game
    }

@app.post("/games/bulk/")
async def list_of_games(games: list[Game]):
    return {
        "list of games": games
    }

@app.post("/games/ratings/")
async def dict_of_ratings(ratings: dict[str, float]):
    return {
        "ratings": ratings
    }