# Content Distribution Service

The Content Distribution Service creates "add" and "remove" caching messages to the system which will be sent to a Kafka broker. This service has two endpoints:
- /add: Takes as arguments "origin": The location of a video file in another server and "title": A human readable title for the video.
- /remove: Takes as an argument "filename": The actual filename of the video file.

An environemtn variable KAFKA_BROKER must be set in the content_distribution_service_deployment.yaml which points to the Kafka broker these caching messages will be sent to.
