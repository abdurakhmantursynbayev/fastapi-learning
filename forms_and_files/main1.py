from fastapi import FastAPI, UploadFile, File
from typing import Annotated

app = FastAPI()

@app.post("/upload")
async def upload(
    files: Annotated[list[UploadFile], File()]
):
    return {
        "filenames": [f.filename for f in files]
    }