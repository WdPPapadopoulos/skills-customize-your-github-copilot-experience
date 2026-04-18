from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for assignment practice.
items = [
    {"name": "Notebook", "price": 2.99, "in_stock": True},
    {"name": "Pen", "price": 1.49, "in_stock": True},
]


class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment API."}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    item_data = item.model_dump()
    items.append(item_data)
    return item_data
