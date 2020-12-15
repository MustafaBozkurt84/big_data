1. See the information of consumer group1
```
[train@localhost data_generator]$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group1

Consumer group 'group1' has no active members.

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID     HOST            CLIENT-ID
group1          topic1          1          48              48              0               -               -               -
group1          topic1          0          64              64              0               -               -               -
group1          topic1          2          53              53              0               -               -               -
```

As you see the lag is 0 which means consumer group1 consumers consumed all messsage and there is no lag.

2. While consumer terminals closed produce iris to topic1 again.
` [train@localhost data_generator]$ python3 dataframe_to_kafka.py -t topic1  `

3. Describe group1 from another terminal and see there is lag
```
[train@localhost manual]$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group1

Consumer group 'group1' has no active members.

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID     HOST            CLIENT-ID
group1          topic1          1          48              90              42              -               -               -
group1          topic1          0          64              121             57              -               -               -
group1          topic1          2          53              92              39              -               -               -
```

4. Start three consumers again and describe again
```
[train@localhost data_generator]$ kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group group1

GROUP           TOPIC           PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG             CONSUMER-ID                                            HOST            CLIENT-ID
group1          topic1          0          124             124             0               consumer-group1-1-5d1d4aea-827f-4aba-9ee4-fdd2d1536d5c /127.0.0.1      consumer-group1-1
group1          topic1          2          98              98              0               consumer-group1-1-d3b22fb2-8e11-4203-bf67-bb3d383b43d4 /127.0.0.1      consumer-group1-1
group1          topic1          1          93              93              0               consumer-group1-1-a4436725-bc42-4bc6-8285-d5e8a9f8da56 /127.0.0.1      consumer-group1-1
```

Lag is 0 again. But the first consumer consumed all lags before we start rest two consumer.

5. Close all three consumer with `Ctrl+C`
