Build image:
docker build -t video-server .

Run container:
docker run -d -p 8000:8000 -v ~/Videos:/app/videos -e VIDEO_FOLDER=/app/videos video-server
