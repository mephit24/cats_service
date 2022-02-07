from fastapi import FastAPI, Request

from api import get_cats_json, create_cat

app = FastAPI()

@app.get("/ping")
def read_root():
    return "Cats Service. Version 0.1"

@app.get("/cats")
def give_cats(offset: int = None, limit: int = None):
    return get_cats_json(offset=offset, limit=limit)

@app.post("/cat")
async def create_new_cat(a: Request):
    status = create_cat(await a.body())
    return {"status":status}

