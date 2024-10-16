from src.server.api import molecules
from fastapi import FastAPI
from os import getenv
import time


app = FastAPI(lifespan=molecules.lifespan)
app.include_router(molecules.router)


@app.get("/")
def get_server():
    # TODO: strictly for showcasing purposes, remove time.sleep() in the next commit
    time.sleep(5)
    return {"server_id": getenv("SERVER_ID")}



