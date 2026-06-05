from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    quantity: int | None = None


class Customer(BaseModel):
    username: str
    email: str


@app.put("/orders/{order_id}")
async def orders(order_id: int, product: Product, customer: Customer):
    return {
        "order_id": order_id,
        "product": product,
        "customer": customer
    }

@app.put("/orders/pc/")
async def produc_customer(product: Product, customer: Customer, priority: Annotated[int, Body()]):
    return {
        "product": product,
        "customer": customer,
        "priority": priority
    }


@app.put("/products/")
async def product_info(product: Annotated[Product, Body(embed= True)]):
    return {
        "product": product
    }
