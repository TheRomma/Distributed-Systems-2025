from confluent_kafka import Producer
import os

#Kafka producer init.
conf = {'bootstrap.servers': os.getenv("KAFKA_BROKER", "localhost:9092")}
producer = Producer(conf)

def produce_add_message(link: str, title: str):
    message = {"link": link, "title": title}
    producer.produce('add', value=str(message))
    producer.flush()

def produce_remove_message(filename: str):
    message = {"filename": filename}
    producer.produce('remove', value=str(message))
    producer.flush()
