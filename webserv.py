from typing import Union

from fastapi import FastAPI, Request
from pydantic.types import PositiveInt

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
