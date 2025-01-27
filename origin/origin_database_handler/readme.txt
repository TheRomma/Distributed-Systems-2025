Build image:
docker build -t origin-db-handler .

Run container:
docker run --network="host" -d -p 27017:27017 origin-db-handler
