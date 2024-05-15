# Kafka

# Zookeeper
## How do the Kafka brokers and clients keep track of all the Kafka brokers if there is more than one? 
- The Kafka team decided to use Zookeeper for this purpose.
- Zookeeper is used for metadata management in the Kafka world. For example:
    - Zookeeper keeps track of which brokers are part of the Kafka cluster
    - Zookeeper is used by Kafka brokers to determine which broker is the leader of a given partition and topic and perform leader elections
    - Zookeeper stores configurations for topics and permissions
    - Zookeeper sends notifications to Kafka in case of changes (e.g. new topic, broker dies, broker comes up, delete topics, etc.…)
- port: 2181:2181

# Kafka Cluster
- 3 kafka cluster
    - bootstrap servers: kafka1:19092, kafka2:19093, kafka3:19094
    - dependency of each cluster is zookeeper
    - image source: confluentinc

# Kafka-UI
- kafka clusters name: local
- port: 8080
- UI: [Open in Browser](localhost:8080)
