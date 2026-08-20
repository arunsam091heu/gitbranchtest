# API endpoints for FastAPI application
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from models import Item, User, ItemResponse
from database import db
from auth import verify_token, create_access_token
from logger import app_logger
import uvicorn

app = FastAPI(title="FastAPI Application", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item, token: dict = Depends(verify_token)):
    """Create a new item"""
    app_logger.info(f"Creating item: {item.name}")
    db.add_item(item.id, item.dict())
    return {
        "success": True,
        "data": item,
        "message": "Item created successfully"
    }

@app.post("/api/items")
async def create_item_simple(item_data: dict):
    """Create item with simple data"""
    return {"message": "Item created", "data": item_data}

@app.get("/items/{item_id}")
def get_item(item_id: int, token: dict = Depends(verify_token)):
    """Get an item by ID"""
    app_logger.info(f"Fetching item: {item_id}")
    item = db.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/", response_model=List[Item])
def list_items(token: dict = Depends(verify_token)):
    """List all items"""
    app_logger.info("Listing all items")
    return db.get_all_items()

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, token: dict = Depends(verify_token)):
    """Update an item"""
    app_logger.info(f"Updating item: {item_id}")
    updated = db.update_item(item_id, item.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@app.delete("/items/{item_id}")
def delete_item(item_id: int, token: dict = Depends(verify_token)):
    """Delete an item"""
    app_logger.info(f"Deleting item: {item_id}")
    if not db.delete_item(item_id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

@app.post("/login")
def login(username: str, password: str):
    """Login endpoint to get access token"""
    app_logger.info(f"Login attempt for user: {username}")
    # Simple validation (in production, verify against database)
    if username and password:
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
