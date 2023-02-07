from typing import Union
import uvicorn
from fastapi import FastAPI, Request
from pydantic.types import PositiveInt

from orm_model import test_db_connection
from recount_statistic import recount_statistic
from api import get_cats_json, create_cat

app = FastAPI()

@app.get("/ping")
def read_root():
    return "Cats Service. Version 0.1"

@app.get("/cats")
def give_cats(offset: PositiveInt = None,
              limit: PositiveInt = None,
              attribute: Union[str, None] = None,
              order: Union[str, None] = None):
    return get_cats_json(offset=offset, limit=limit, attribute=attribute, order=order)

@app.post("/cat")
async def create_new_cat(a: Request):
    status = create_cat(await a.body())
    return {"status":status}

@app.get("/recount") # TODO: need request limiter
async def recount():
    return recount_statistic()

if __name__ == "__main__":
    if test_db_connection():
        recount_statistic()
        uvicorn.run("webserv:app", host="0.0.0.0", port=8080, log_level="info")
