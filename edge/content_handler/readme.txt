Build image:
docker build -t edge-content-handler .

Run container:
docker run --network="host" -d -v /path/to/videos:/app/videos edge-content-handler
