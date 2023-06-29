#!/usr/bin/python3

from celery import Celery
import json
from kafka_client import kafka_wrapper

app = Celery('producer', broker='redis://localhost:6379/0')

@app.task
def produce_to_kafka():
    # Read JSON data from file
    with open('File1.json') as json_file:
        data = json.load(json_file)

    # Send JSON data to Kafka
    num_messages = 100

    # with KafkaWrapper(bootstrap_servers, topic) as kafka:
    with kafka_wrapper as kafka:
        for item in range(num_messages):
            message = json.dumps(data)
            kafka.produce(message)