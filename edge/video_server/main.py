from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import os

app = FastAPI()

# Metrics
VIDEO_REQUEST_COUNT = Counter('video_requests_total', 'Total video requests', ['filename'])
VIDEO_SIZE_HISTOGRAM = Histogram('video_size_bytes', 'Video file size in bytes')
VIDEO_SERVING_TIME = Histogram('video_serving_seconds', 'Time taken to serve video')
ERROR_COUNT = Counter('video_errors_total', 'Total video serving errors', ['error_type'])

@app.get("/videos/{filename}")
async def get_video(filename: str):
    try:
        file_path = os.path.join(os.getenv("VIDEO_FOLDER", "videos"), filename)
        
        if os.path.exists(file_path):
            VIDEO_REQUEST_COUNT.labels(filename=filename).inc()
            VIDEO_SIZE_HISTOGRAM.observe(os.path.getsize(file_path))
            
            with VIDEO_SERVING_TIME.time():
                return FileResponse(file_path)
        else:
            ERROR_COUNT.labels(error_type="not_found").inc()
            raise HTTPException(status_code=404, detail="File not found")
            
    except Exception as e:
        ERROR_COUNT.labels(error_type="server_error").inc()
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)