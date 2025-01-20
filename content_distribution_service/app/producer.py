from confluent_kafka import Producer

conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(conf)

def produce_add_message(link: str, title: str):
    message = {"link": link, "title": title}
    producer.produce('add', value=str(message))
    producer.flush()

def produce_remove_message(filename: str):
    message = {"filename": filename}
    producer.produce('remove', value=str(message))
    producer.flush()
