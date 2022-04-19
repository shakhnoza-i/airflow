import time
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse


app = FastAPI()


@app.post("/search/")
def read_file():
    time.sleep(60)
    return FileResponse("response_b.json")
