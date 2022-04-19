import time
from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI()


@app.post("/search/")
def read_file():
    time.sleep(30)
    return FileResponse("response_a.json")
