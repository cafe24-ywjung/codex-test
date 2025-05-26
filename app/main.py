from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.future import select

from .database import get_db
from .models import Base, Item, engine

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items", response_model=List[dict])
async def read_items(db=Depends(get_db)):
    result = await db.execute(select(Item))
    items = result.scalars().all()
    return [
        {"id": item.id, "name": item.name, "price": item.price}
        for item in items
    ]

def main():
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    main()