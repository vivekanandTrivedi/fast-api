from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    quantity : int

item : List[Item] = []

@app.get("/")
def read_root():
    return {"msg": "Returning root"}

@app.get("/items")
def return_all_items():
    return {"Items" : item}

@app.post("/items")
def add_item(items : Item):
    item.append(items)
    return item

@app.put("/items/{name}")
def update_item(name: str, items: Item):
    for name in items:
        if name == name:
            item.append(items)
            return item
    return {"msg": "Item not found"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/vendor")
def query_params(name: str = None):
    return {"name" : name}

@app.get("/products")
def query_params(limit: int = 10, name : str = None):
    return {
        "limit" : limit,
        "name" : name
    }

class Country(BaseModel):
    country_name : str
    country_code : int

class Vendor(BaseModel):
    name: str
    email: str
    password: str
    country_of_origin: Country

@app.post("/vendor")
def create_user(vendor : Vendor):
    return {
        "data" : vendor
    }
