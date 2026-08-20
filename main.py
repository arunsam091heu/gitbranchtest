from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="FastAPI Application", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}


@app.get("/api/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.post("/api/items")
async def create_item(item_data: dict):
    return {"message": "Item created", "data": item_data}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
