1. If you sent key to topic you can guarantee same key goes to same partition.

2. Start 3 consumer with following command
`  [train@localhost manual]$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --property print.key=true --group group1  `

3. With data generator produce iris to topic1 twice (data_generator is able to send keys to kafka).

4. Observe that same keys goes to same partitions (because three partitions consumed by three consumers) For example you will see 115 key twice from same consumer.

