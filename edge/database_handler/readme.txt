Build image:
docker build -t edge-db-handler .

Run container:
docker run --network="host" -d -p 27017:27017 edge-db-handler
