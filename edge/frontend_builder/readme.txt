# Edge Frontend Builder

Edge Frontend Builder is a service that recreates a simple html document containing a list of video files stored within the system. Two environment variables must be set in edge_node_deployment.yaml:
- MONGO_SERVICE: Points to the mongodb service responsible for all the mongodb instances.
- SLEEP_INTERVAL: Interval in seconds at which the frontend will be rebuilt.
