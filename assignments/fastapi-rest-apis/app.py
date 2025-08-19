from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(title="FastAPI Assignment API")

class ItemBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    price: float = Field(ge=0)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    price: Optional[float] = Field(default=None, ge=0)

class Item(ItemBase):
    id: int

items: List[Item] = []
next_id = 1

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/items", response_model=List[Item])
def list_items(q: Optional[str] = None, min_price: Optional[float] = None, max_price: Optional[float] = None):
    results = items
    if q:
        results = [i for i in results if q.lower() in i.name.lower() or (i.description and q.lower() in i.description.lower())]
    if min_price is not None:
        results = [i for i in results if i.price >= min_price]
    if max_price is not None:
        results = [i for i in results if i.price <= max_price]
    return results

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for i in items:
        if i.id == item_id:
            return i
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", status_code=201, response_model=Item)
def create_item(payload: ItemCreate):
    global next_id
    item = Item(id=next_id, **payload.dict())
    next_id += 1
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemUpdate):
    for idx, existing in enumerate(items):
        if existing.id == item_id:
            data = existing.dict()
            update_data = payload.dict(exclude_unset=True)
            data.update(update_data)
            updated = Item(**data)
            items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for idx, existing in enumerate(items):
        if existing.id == item_id:
            del items[idx]
            return
    raise HTTPException(status_code=404, detail="Item not found")
