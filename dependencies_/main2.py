from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

#1-practice task

def get_number(
        number: int
):
    return number

def double_number(number: Annotated[int, Depends(get_number)]):
    return (2*number)

def square_number(number: Annotated[int, Depends(get_number)]):
    return (number ** 2)

@app.get("/number")
async def calculating_number(double_n: Annotated[int, Depends(double_number)], square_n: Annotated[int, Depends(square_number)]):
    return {
        "double": double_n,
        "square": square_n
    }

#2-practice task

def get_token(token: str):
    return token

def current_user(token: Annotated[str, Depends(get_token)]):
    #тут используя token мы будем узнать кто current user
    #и должны вернуть user но у нас его нет так что вернем самого токен снова
    return token

def active_user(user: Annotated[str, Depends(current_user)]):
    #а тут мы должны были взять current user data а потом знать он active or deactive
    return user

def admin_user(a_user: Annotated[str, Depends(active_user)]):
    return a_user

@app.get("/admin")
async def read_admin(admin: Annotated[str, Depends(admin_user)]):
    return {
        "admin": admin
    }

#3-practice task

def get_user(user: str):
    return user

def check_admin(admin: Annotated[str, Depends(get_user)]):
    return admin
def check_premium(prem: Annotated[str, Depends(get_user)]):
    return prem

@app.get("/users/user")
async def read_user(admin: Annotated[str, Depends(check_admin)], prem: Annotated[str, Depends(check_premium)]):
    return {
        "admin": admin,
        "prem": prem
    }

