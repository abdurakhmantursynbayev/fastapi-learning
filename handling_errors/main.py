from fastapi import FastAPI, HTTPException


app = FastAPI()

#1-practice-task

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id == 1:
        return {"name": "laptop"}
    raise HTTPException(
        status_code=404,  #not found = 404
        detail="Item not found"
    )
#2-practice task

@app.get("/adult/{age}")
async def get_age(age: int):
    if age < 18:
        raise HTTPException(
            status_code=403, #forbidden = 403
            detail="Access denied"
        )
    return {
        "message": "access granted"
    }

#3-practice task

@app.get("/temperature/{temp}")
async def get_temp(temp: float):
    if temp > 100:
        raise HTTPException(
            status_code=400,
            detail="temperature too high"
        )
    elif temp < -100:
        raise HTTPException(
            status_code=400,
            detail="temperature too low"
        )
    return {
        "temperature": temp
    }

#4-practice task

@app.get("/products/{product_id}")
async def get_poduct_id(product_id: int):
    if product_id == 1:
        return {
            "id": 1,
            "name": "Iphone"
        }
    raise HTTPException(
        status_code=404,
        detail={
            "message": "product not found",
            "product id": product_id
        }
    )

#5-practice task

@app.get("/score/{score}")
async def get_score(score: int):
    if score < 0:
        raise HTTPException(
            status_code=400,
            detail="score cannot be negative"
        )
    elif score>100:
        raise HTTPException(
            status_code=400,
            detail="score cannot exceed 100"
        )
    return {
        "score": score,
        "status": "valid"
    }