from confluent_kafka import Consumer, KafkaError
from database import add_entry, remove_entry
import os

#Kafka consumer init.
conf = {
    'bootstrap.servers': os.getenv("KAFKA_BROKER", "localhost:9092"),
    'group.id': "database-service-group",
    'auto.offset.reset': 'latest'
}

consumer = Consumer(conf)
consumer.subscribe(['add', 'remove'])

def consume_messages():
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        topic = msg.topic()
        message = eval(msg.value().decode('utf-8'))

        if topic == 'add':
            add_entry(message['link'], message['title'])
        elif topic == 'remove':
            remove_entry(message['filename'])

    consumer.close()
