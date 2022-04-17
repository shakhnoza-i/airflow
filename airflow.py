from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse


app = FastAPI()


@app.post("/search/")
async def search():
    # time.sleep(60)
    return FileResponse("response_b.json")
