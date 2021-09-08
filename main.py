import uvicorn
from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

from dummy_models import Item, Plan, Task
import postgres_service

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hi"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    print(item)
    return item

@app.post("/plan")
async def create_plan(plan:Plan):
    print(plan)
    return(plan)




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)