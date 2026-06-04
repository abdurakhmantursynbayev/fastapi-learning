from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get("/games/{game_id}/")
async def game_id(game_id: Annotated[int, Path(gt = 0)], gamename: Annotated[str | None, Query(deprecated=True, alias = "game-name")]):
    result = {"game_id": game_id}
    if gamename:
        result.update({"game-name": gamename})
    return result

@app.get("/games/search/")
async def game_search(name: Annotated[str, Query(min_length=3, max_length=20)]):
    data = {} #here will be data that wad founded by searching by name
    return {
        "searched by": name,
        "data": data
    }

@app.get("/users/{user_id}/reviews/{review_id}/")
async def review(user_id: Annotated[int, Path(ge = 1)], review_id: Annotated[int, Path(ge=1)],
                 review_info: Annotated[str | None, Query(alias = "review-info", title = "information", description="information about review")] = None):
    return {
        "user_id": user_id,
        "review_id": review_id,
        "review_info": review_info
    }
@app.get("/discount/{percent}")
async def discount_percent(percent: Annotated[float, Path(ge = 1, le = 99)]):
    return {"discount": percent}

@app.get("/games/search/filter")
async def search_filter(filter: Annotated[list[str], Query(title="filters", description="filters for searching, here might be names, prices, discounts")]):
    return {
        "filter": filter
    }