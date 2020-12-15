1. List topics
`kafka-topics.sh --bootstrap-server localhost:9092 --list `

2. Create a topic
```
[train@localhost play]$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic topic1 --replication-factor 1 --partitions 3
Created topic topic1.
```

3. Describe a topic
```
[train@localhost play]$ kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic topic1
Topic: topic1   PartitionCount: 3       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: topic1   Partition: 0    Leader: 0       Replicas: 0     Isr: 0
        Topic: topic1   Partition: 1    Leader: 0       Replicas: 0     Isr: 0
        Topic: topic1   Partition: 2    Leader: 0       Replicas: 0     Isr: 0
```
Leader: 0 means broker-id 0 is leader for this partitions.
Replicas: 0 means there is no other replica because we have just one broker.

4. Delete a topic
```
[train@localhost play]$ kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic topic1
[train@localhost play]$ kafka-topics.sh --bootstrap-server localhost:9092 --list
```
- Delete multiple topics: `--topic topic1,topic2,...,topicN`

5. Try create a topic with 3 replicas
```
[train@localhost play]$ kafka-topics.sh --bootstrap-server localhost:9092 --create --topic topic1 --replication-factor 3 --partitions 3
Error while executing topic command : org.apache.kafka.common.errors.InvalidReplicationFactorException: Replication factor: 3 larger than available brokers: 1.
[2020-09-18 23:31:38,299] ERROR java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.InvalidReplicationFactorException: Replication factor: 3 larger than available brokers: 1.
        at org.apache.kafka.common.internals.KafkaFutureImpl.wrapAndThrow(KafkaFutureImpl.java:45)
        at org.apache.kafka.common.internals.KafkaFutureImpl.access$000(KafkaFutureImpl.java:32)
        at org.apache.kafka.common.internals.KafkaFutureImpl$SingleWaiter.await(KafkaFutureImpl.java:89)
        at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:260)
        at kafka.admin.TopicCommand$AdminClientTopicService.createTopic(TopicCommand.scala:244)
        at kafka.admin.TopicCommand$TopicService.createTopic(TopicCommand.scala:196)
        at kafka.admin.TopicCommand$TopicService.createTopic$(TopicCommand.scala:191)
        at kafka.admin.TopicCommand$AdminClientTopicService.createTopic(TopicCommand.scala:219)
        at kafka.admin.TopicCommand$.main(TopicCommand.scala:62)
        at kafka.admin.TopicCommand.main(TopicCommand.scala)
Caused by: org.apache.kafka.common.errors.InvalidReplicationFactorException: Replication factor: 3 larger than available brokers: 1.

```
Since we have just one broker we cannot create topic with greater than 1 replica.

6. We can use zookeeper instead of bootstrap-server but it is deprecated. You may have to use zookeeper older versions of Kafka.
See topics.sh help menu that zookeeper deprecated: `[train@localhost play]$ kafka-topics.sh`