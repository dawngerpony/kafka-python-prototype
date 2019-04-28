Kafka Python prototype
======================

From https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05:

Prerequisites
-------------

1. Download and unzip Kafka from https://kafka.apache.org/quickstart.

Getting started
---------------

1. Start up single-node Kafka and Zookeeper:

        cd kafka-stack-docker-compose
        docker-compose -f zk-single-kafka-single.yml up

2. Create and enter virtualenv:

        virtualenv .venv
        source .venv/bin/activate

3. Create a topic called 'test':

        bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

4. Run the consumer script, which will subscribe to the topic and print any messages
   that are published to the topic:

        python consume.py

5. Publish a message onto the topic using the publish script:

        python publish.py

6. You should 