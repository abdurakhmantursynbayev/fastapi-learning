from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[Item,
                    Body(
                        examples=[
                            {
                                "name": "foo",
                                "description": "a very nice item",
                                "price": 55.5,
                                "tax": 5.4
                            }
                        ]
                    )]
):
    return {
        "item id": item_id,
        "item": item
    }