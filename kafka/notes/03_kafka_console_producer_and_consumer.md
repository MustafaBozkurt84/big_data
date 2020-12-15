1. Send messages to topic1 with kafka-console.producer.sh

In terminal-1 :
```
[train@localhost play]$ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic1
hello this is first message
>this is second one
>this will be 3'rd msg
>
```

2. Consume messages from topic1
In terminal-2:
```
[train@localhost manual]$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --from-beginning
hellothis is first message
this is second one
this will be 3'rd msg
```

3. Close both terminal with Ctrl+C

4. If you produce messages to non-existing topic that topic will be created upon first message arriving but it will be created with default properties which is not recommended.

5. Producing messages with key in terminal-1
```
[train@localhost play]$ kafka-console-producer.sh --bootstrap-server localhost:9092 --topic topic1 --property parse.key=true --property key.separator=,
key1,> message-1
>ky-2, message-2
>key-3,message-3
>
```

6. Consuming with key in terminal-2
```
[train@localhost manual]$ kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --property print.key=true --property key.separator=,
null,this is second one
null,hellothis is first message
null,this will be 3'rd msg
key1, message-1
ky-2, message-2
key-3,message-3
```

7. Close both terminal Ctrl+C

