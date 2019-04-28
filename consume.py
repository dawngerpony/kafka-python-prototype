from kafka import KafkaConsumer

TOPIC_NAME = 'test'

consumer = KafkaConsumer(TOPIC_NAME)

for msg in consumer:
    print(msg)
