from re import L
from fastapi import FastAPI


app = FastAPI()


@app.get("/healthcheck")
async def health():
    """Check if server is alive"""
    return {"alive": True}


@app.get("/get_token")
async def get_token():
    """Returns jwt token"""
    return {"token": "1234"}


@app.get("/todos")
async def todos():
    """Returns the list of todos"""
    return {"todo": ["Run server in docker"]}
