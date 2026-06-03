from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def message():
    return {"message":"Hello"}

@app.get("/about")
async def about_user():
    return {
        "name": "abdurakhman",
        "profession": "Future Backend developer"
    }

@app.get("/contact")
async def contacts():
    return {"telegram": "user100",
            "email": "abdu@gmail.com"
            }

