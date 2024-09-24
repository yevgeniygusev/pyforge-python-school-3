from src.server.api import molecules
from fastapi import FastAPI


app = FastAPI(lifespan=molecules.lifespan)
app.include_router(molecules.router)


@app.get("/")
def root():
    return {"message": "Heyo"}



