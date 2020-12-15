1. Check if hive metastore is running  
```
[train@localhost play]$ pgrep -f org.apache.hive.service.server.HiveServer2
226646
```
If you can't see pid no as output run `start-all.sh`  
2. Check if hiveserver2 is running  
```
[train@localhost play]$ pgrep -f org.apache.hadoop.hive.metastore.HiveMetaStore
226957
```
If you can't see pid no as output run `start-all.sh`  

3. Beeline connection  
`[train@localhost play]$ beeline -u jdbc:hive2://127.0.0.1:10000`

You should see `0: jdbc:hive2://127.0.0.1:10000>` means beeline shell is ready to use.  
Close logs  
`0: jdbc:hive2://127.0.0.1:10000> set hive.server2.logging.operation.level=NONE;`  

4. List databases
```
0: jdbc:hive2://localhost:10000> show databases;
+----------------+
| database_name  |
+----------------+
| bookstore      |
| default        |
| train          |
+----------------+
3 rows selected (0.078 seconds)
```

5. Select a database and list table in it.
```
0: jdbc:hive2://localhost:10000> use bookstore;
No rows affected (0.066 seconds)
0: jdbc:hive2://localhost:10000> show tables;
+-----------+
| tab_name  |
+-----------+
| books     |
+-----------+
1 row selected (0.081 seconds)
```

6. exit from beeline
`!q`