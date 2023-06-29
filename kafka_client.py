from kafka import KafkaConsumer, KafkaProducer

# Kafka cluster settings
bootstrap_servers = ["localhost:9092",]
topic = "dataak_topic"

class KafkaWrapper:
    def __init__(self, bootstrap_servers, topic):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.consumer = None
        self.producer = None

    def __enter__(self):
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: x.decode('utf-8')
        )

        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda x: x.encode('utf-8')
        )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.consumer is not None:
            self.consumer.close()

        if self.producer is not None:
            self.producer.close()

    def consume(self):
        for message in self.consumer:
            yield message.value

    def produce(self, message):
        self.producer.send(self.topic, value=message)

# # Example usage:
# bootstrap_servers = 'localhost:9092'
# topic = 'my-topic'

# with KafkaWrapper(bootstrap_servers, topic) as kafka:
#     # Producer
#     kafka.produce('Hello, Kafka!')

#     # Consumer
#     for message in kafka.consume():
#         print(message)

kafka_wrapper = KafkaWrapper(bootstrap_servers, topic)