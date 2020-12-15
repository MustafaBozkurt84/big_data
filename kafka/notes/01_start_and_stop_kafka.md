## Start Kafka

1. Start zookeeper
` [train@localhost play]$ zookeeper-server-start.sh -daemon /opt/manual/kafka/config/zookeeper.properties  `

2. Start kafka server
` [train@localhost play]$ kafka-server-start.sh -daemon /opt/manual/kafka/config/server.properties  `

3. Check if zookeeper and kafka run
```
[train@localhost play]$ lsof -i -P -n | grep 2181
java      927 train  117u  IPv6 281435      0t0  TCP *:2181 (LISTEN)
java      927 train  121u  IPv6 281514      0t0  TCP 127.0.0.1:2181->127.0.0.1:45258 (ESTABLISHED)
java     1344 train  117u  IPv6 288053      0t0  TCP 127.0.0.1:45258->127.0.0.1:2181 (ESTABLISHED)


[train@localhost play]$ lsof -i -P -n | grep 9092
java    16117 train  122u  IPv6 177761      0t0  TCP *:9092 (LISTEN)
java    16117 train  138u  IPv6 177766      0t0  TCP 127.0.0.1:55696->127.0.0.1:9092 (ESTABLISHED)
java    16117 train  139u  IPv6 176673      0t0  TCP 127.0.0.1:9092->127.0.0.1:55696 (ESTABLISHED)
```

## Stop Kafka

4. Stop kafka first then zookeeper
```
[train@localhost play]$ kafka-server-stop.sh
[train@localhost play]$ zookeeper-server-stop.sh
```
