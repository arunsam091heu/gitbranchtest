# FastAPI Application

A simple FastAPI application with basic endpoints.

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Documentation

- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

## Endpoints

- `GET /` - Welcome message
- `GET /api/health` - Health check
- `GET /api/items/{item_id}` - Get an item by ID
- `POST /api/items` - Create a new item
