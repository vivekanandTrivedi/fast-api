from fastapi import FastAPI
from pydantic import BaseModel

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