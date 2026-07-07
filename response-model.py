from os import name

from fastapi import FastAPI, status, HTTPException,Request
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from starlette.requests import Request

app = FastAPI()

class UserInput(BaseModel):
    name: str
    email: str
    password: int

class UserResponse(BaseModel):
    name: str
    email: str

@app.get("/user", response_model=UserResponse)
def user():
    return{
        "name": "sumit",
        "email": "harsh@123",
        "password": 12345
    }
@app.post("/user", status_code= status.HTTP_201_CREATED)
def create_user():
    return{"msg" : "user created"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND)
    return{
        "name": "sumit",
        "email": "harsh@123",
    }

class UserNotFound(Exception):
    def __init__(self, cos_id: int):
        self.cos_id = cos_id

@app.exception_handler(UserNotFound)
def user_not_found(request: Request, exc: UserNotFound):
    return JSONResponse(
        status_code= 400,
        content={"message": exc.cos_id}
    )

@app.get("/user/cos/{cos_id}")
def get_user_cos_id(cos_id: int):
    if cos_id != 1:
        raise UserNotFound(cos_id)
    return{
        "name" : cos_id
    }

