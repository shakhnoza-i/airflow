import time
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.get("/")
def index ():
    return "Hello world!"


@app.post("/search/")
async def read_file():
    # time.sleep(30)
    return FileResponse("response_a.json")
