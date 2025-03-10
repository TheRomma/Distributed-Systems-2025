from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

#Prometheus instrumentator.
Instrumentator().instrument(app).expose(app)

VIDEO_FOLDER = "/app/videos"

#Servers videos from the edge node.
@app.get("/videos/{filename}")
async def get_video(filename: str):
    file_path = os.path.join(VIDEO_FOLDER, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")
