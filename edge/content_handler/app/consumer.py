from confluent_kafka import Consumer, KafkaError
from file_manager import handle_add_message, handle_remove_message
import os

conf = {
    'bootstrap.servers': os.getenv("KAFKA_BROKER", "localhost:9092"),
    'group.id': os.getenv("HOSTNAME", "file-manager-group")+"_content_handler",
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
            handle_add_message(message['link'], message['title'])
        elif topic == 'remove':
            handle_remove_message(message['filename'])

    consumer.close()
