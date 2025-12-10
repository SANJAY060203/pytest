from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

@app.get("/ping")
def ping():
    return {"pong": True}

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    return Item(id=item_id, name=f"Item {item_id}", price=9.99)

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    return item
