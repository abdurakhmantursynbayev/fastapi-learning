from fastapi import FastAPI, Query
from enum import Enum
from typing import Annotated

class sorting_data(str, Enum):
    rating = "rating"
    price = "price"
    name = "name"


app = FastAPI()

@app.get("/games/search/")
async def searching(search_query: Annotated[str | None,
                                            Query(alias = "search",
                                            min_length=3,
                                            max_length=30,
                                            title = "Game search",
                                            description="search game by title")] = None):
    return {
        "message": "nothing",
        "search query": search_query
    }

@app.get("/games/search/platforms/")
async def platform_s(platform: Annotated[list[str] | None, Query()] = None):
    return {
        "platforms": platform
    }

@app.get("/games/sort/")
async def sorting(sort_by: sorting_data):
    if sort_by is sorting_data.rating:
        return {
            "sort by": sort_by
        }
    elif sort_by.value == "price":
        return {
            "sort by": "price"
        }
    return {
        "sort by": "name"
    }

@app.get("/games/name/")
async def name_of_game(game_name: Annotated[str | None, Query(deprecated=True)] = None, name_g: Annotated[str | None, Query(min_length=3, pattern = "^[A-Za-z]+$")] = None):
    return {
        "game name": game_name,
        "name of game": name_g
    }

