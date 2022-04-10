from fastapi import FastAPI, Request
import uvicorn
from orm_model import test_db_connection
from recount_statistic import recount_statistic

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

@app.get("/recount") #debt: restrict frecuent requests
async def recount():
    return recount_statistic()

if __name__ == "__main__":
    if test_db_connection():
        uvicorn.run("webserv:app", host="127.0.0.1", port=8080, log_level="info")
    print('Configuration database connect was corrupted and will remove, restart application!')

