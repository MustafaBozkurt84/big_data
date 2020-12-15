1. In terminal-1 start producer
`kafka-console-producer --bootstrap-server localhost:9092 --topic topic1  `

2. In terminal-2, 3, and 4 start consumer under a group name
```
[train@localhost manual]$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --group group1
```


3. In terminal-1 write messages and observe results from consumer terminals (2,3,4)
```
>message-1
>message-2
>message-3
>message-4
>message-5
>message-6
>message-7
>message-8
>message-9
```

4. Messages consumed by each consumer under group1 round robin fashion.

5. `Ctrl+C` to terminal-1 (producer) and from data_generator produce iris dataset to topic1
`(venvspark) [train@localhost data_generator]$ python dataframe_to_kafka.py -t topic1  `

Observe the consumer terminals and see how iris rows consumed by each consumer


6. Close consumer terminals with `Ctrl+C`

7. reset consumer group
First run describe then --dry-run see the result. If it is ok lastly run with --execute
```
[train@localhost ~]$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group group1 --describe

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                            HOST            CLIENT-ID
group1          topic1          2          432             432             0               consumer-group1-1-f11ee1de-42ce-4d9d-85d5-736799180455 /127.0.0.1      consumer-group1-1
group1          topic1          1          416             416             0               consumer-group1-1-d32fb248-00e9-40e9-97a9-e2c22c986cac /127.0.0.1      consumer-group1-1
group1          topic1          0          559             559             0               consumer-group1-1-3725d3cd-8f1e-42dd-8f64-d1a59e711af6 /127.0.0.1      consumer-group1-1
```

```
[train@localhost ~]$  kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group group2 --reset-offsets --to-earliest --dry-run --topic topic1

GROUP                          TOPIC                          PARTITION  NEW-OFFSET
group2                         topic1                         0          0
group2                         topic1                         1          0
group2                         topic1                         2          0
```

```
[train@localhost ~]$  kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group group2 --reset-offsets --to-earliest --execute --topic topic1

GROUP                          TOPIC                          PARTITION  NEW-OFFSET
group2                         topic1                         0          0
group2                         topic1                         1          0
group2                         topic1                         2          0
[train@localhost ~]$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group group2 --describe

Consumer group 'group2' has no active members.

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID     HOST            CLIENT-ID
group2          topic1          1          0               416             416             -               -               -
group2          topic1          0          0               559             559             -               -               -
group2          topic1          2          0               432             432             -               -               -
```

