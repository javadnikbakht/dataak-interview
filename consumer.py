from elasticsearch import Elasticsearch
from kafka_client import kafka_wrapper
from elastic_client import index_name, elastic


with kafka_wrapper as kafka, elastic as es:
    while True:
        for message in kafka.consume():
            es.index(index=index_name, body=message)


