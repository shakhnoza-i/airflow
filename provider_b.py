import time
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse


app = FastAPI()


@app.post("/search/")
async def read_file():
    # time.sleep(60)
    return FileResponse("response_b.json")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile("response_b.json")):
    contents = await file.read()
    return contents
