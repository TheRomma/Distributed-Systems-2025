from fastapi import FastAPI
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from app.producer import produce_add_message, produce_remove_message
import time

app = FastAPI()

# Define metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency')
MESSAGE_COUNT = Counter('kafka_messages_total', 'Total Kafka messages sent', ['topic'])

@app.post("/add")
async def add_message(link: str, title: str):
    REQUEST_COUNT.labels(method='POST', endpoint='/add').inc()
    
    with REQUEST_LATENCY.time():
        produce_add_message(link, title)
        MESSAGE_COUNT.labels(topic='add').inc()
    
    return {"status": "Message sent to 'add' topic"}

@app.post("/remove")
async def remove_message(filename: str):
    REQUEST_COUNT.labels(method='POST', endpoint='/remove').inc()
    
    with REQUEST_LATENCY.time():
        produce_remove_message(filename)
        MESSAGE_COUNT.labels(topic='remove').inc()
    
    return {"status": "Message sent to 'remove' topic"}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)