Build image:
docker build -t edge-content-requester .

Run container:
docker run --network="host" -d -v /path/to/videos:/app/videos edge-content-requester
