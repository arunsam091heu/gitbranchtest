from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class ItemResponse(BaseModel):
    success: bool
    data: Item
    message: str
