Kafka Python prototype
======================

Inspired by an excellent article: [Getting started with Apache Kafka in Python](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05).

Prerequisites
-------------

Technologies:

* Python 3 + virtualenv + pip
* Docker + docker-compose

Additional steps:

1. Download and unzip Kafka from https://kafka.apache.org/quickstart.
2. Clone the excellent [kafka-stack-docker-compose](https://github.com/simplesteph/kafka-stack-docker-compose)
   git repository, to get yourself an easy Docker-based Kafka/Zookeeper installation.

Getting started
---------------

1. Start up single-node Kafka and Zookeeper:

        cd kafka-stack-docker-compose
        docker-compose -f zk-single-kafka-single.yml up

2. Create and enter virtualenv:

        virtualenv .venv
        source .venv/bin/activate
        pip install -r requirements.txt

3. Create a topic called 'test':

        bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

4. Run the consumer script, which will subscribe to the topic and print any messages
   that are published to the topic:

        python consume.py

5. Publish a message onto the topic using the publish script:

        python publish.py

6. You should see your message printed out in the stdout (standard output) console of the consume script!

Resources
---------

* [Apache Avro™ 1.8.2 Getting Started (Python)](https://avro.apache.org/docs/current/gettingstartedpython.html)
