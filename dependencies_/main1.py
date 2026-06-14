# Classes as dependencies

from fastapi import FastAPI, Depends
from typing import Annotated


#1-practice task
class SearchParams:
    def __init__(self, page: int, search: str | None = None):
        self.page = page
        self.search = search

app = FastAPI()

@app.get("/books/")
async def read_book(book: Annotated[SearchParams, Depends()]):
    return {
        "page": book.page,
        "search": book.search
    }

#2-practice task

class PaginationParams:
    def __init__(self,
                skip: int,
                limit: int
    ):
        self.skip = skip
        self.limit = limit
    
@app.get("/users/")
async def read_user(commons: Annotated[PaginationParams, Depends()]):
    return {
        "skip": commons.skip,
        "limit": commons.limit
    }

#3-practice task

class ProductFilter:
    def __init__(self,
                 min_price: int,
                 max_price: int,
                 category: str | None = None,
    ):
        self.min_price = min_price
        self.max_price = max_price
        self.category = category

@app.get("/products")
async def read_product(product: Annotated[ProductFilter, Depends()]):
    response = {}
    if product.category:
        response.update({"category": product.category})
    response.update(
        {
            "min_price": product.min_price,
            "max_price": product.max_price
        }
    )
    return response

#4-practice task

class CommonQueryParams:
    def __init__(
            self,
            skip: int,
            limit: int,
            query: str | None = None, 
    ):
        self.skip = skip
        self.limit = limit
        self.query = query
    
@app.get("/items")
async def read_item(commons: Annotated[CommonQueryParams, Depends()]):
    #тут будет запрос на дб и оттуда сортируем по query и берем считанные данные смотря на skip and limit
    return {
        "skip": commons.skip,
        "limit": commons.limit,
        "query": commons.query
    }

@app.get("/users/user")
async def read_user(commons: Annotated[CommonQueryParams, Depends()]):
    return commons