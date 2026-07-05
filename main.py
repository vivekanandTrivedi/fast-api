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

