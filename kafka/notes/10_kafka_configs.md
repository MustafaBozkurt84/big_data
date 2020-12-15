1. We can configure Kafka in different ways.
If we want to change something cluster wide, we need to modify server.properties file.
We can change configuration per topic but not everything.

2. There is kafka-configs.sh to configure commandline
2.1. Decrease topic retention
```
kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --alter --entity-name topic1 --add-config retention.ms=1000
```
2.2. Change cleanup.policy
```
kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name topic1 \
--alter --add-config cleanup.policy='delete'
```
2.3. Change message retention size to 200 MB
```
kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name topic1 \
--alter --add-config retention.bytes=209715200

```
2.4. Change retention time to 1.67 minutes
```
kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name topic1 --alter --add-config retention.ms=100000
```
See the dynamic configs for a given topic
```
[train@localhost play]$ kafka-configs.sh --bootstrap-server localhost:9092 --entity-type topics --entity-name topic1 --describe
Dynamic configs for topic topic1 are:
  cleanup.policy=delete sensitive=false synonyms={DYNAMIC_TOPIC_CONFIG:cleanup.policy=delete, DEFAULT_CONFIG:log.cleanup.policy=delete}
  retention.ms=100000 sensitive=false synonyms={DYNAMIC_TOPIC_CONFIG:retention.ms=100000}
  retention.bytes=209715200 sensitive=false synonyms={DYNAMIC_TOPIC_CONFIG:retention.bytes=209715200, DEFAULT_CONFIG:log.retention.bytes=-1}

```

3. how many messages in the topic
```
[train@localhost ~]$ kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092  --topic topic1 --time -1 --offsets 1 | awk -F  ":" '{sum += $3} END {print sum}'
1407
```

4. How to truncate a topic? Delete and create with same name
```
[train@localhost ~]$ kafka-topics.sh --bootstrap-server localhost:9092 --topic topic1 --delete
[train@localhost ~]$ kafka-topics.sh --bootstrap-server localhost:9092 --topic topic1 --create --partitions 3 --replication-factor 1
Created topic topic1.
[train@localhost ~]$ kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list localhost:9092  \
--topic topic1 --time -1 --offsets 1 | awk -F  ":" '{sum += $3} END {print sum}'
0
```
