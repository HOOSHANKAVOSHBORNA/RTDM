# Kafka

# Kafka Cluster
- 3 kafka cluster
    - bootstrap servers: kafka1:19092, kafka2:19093, kafka3:19094
    - dependency of each cluster is zookeeper
    - image source: confluentinc

- Run this before docker up:
```bash
sudo chown -R 1001 kafka-persistence  
```
# Kafka-UI
- kafka clusters name: local
- port: 8080
- UI: [Open in Browser](localhost:8080)
