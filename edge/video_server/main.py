from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

VIDEO_FOLDER = "/app/videos"

#@app.on_event("startup")
#async def startup():
#    Instrumentator().instrument(app).expose(app)

@app.get("/videos/{filename}")
async def get_video(filename: str):
    file_path = os.path.join(VIDEO_FOLDER, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")
#
#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="0.0.0.0", port=80)
