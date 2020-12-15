1. Create database
`0: jdbc:hive2://localhost:10000> create database test1;`

2. List databases
```
0: jdbc:hive2://localhost:10000> show databases;
+----------------+
| database_name  |
+----------------+
| bookstore      |
| default        |
| test1          |
| train          |
+----------------+
4 rows selected (0.086 seconds)
```

3. Describe database
```
0: jdbc:hive2://localhost:10000> describe database test1;
+----------+----------+----------------------------------------------------+-------------+-------------+-------------+
| db_name  | comment  |                      location                      | owner_name  | owner_type  | parameters  |
+----------+----------+----------------------------------------------------+-------------+-------------+-------------+
| test1    |          | hdfs://localhost:9000/user/hive/warehouse/test1.db | train       | USER        |             |
+----------+----------+----------------------------------------------------+-------------+-------------+-------------+
1 row selected (0.077 seconds)
```

4. Drop database
```
0: jdbc:hive2://localhost:10000> drop database test1;
No rows affected (0.302 seconds)


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

5. We can add comments to databases
```
0: jdbc:hive2://localhost:10000> create database if not exists test1 comment 'This db is for big data training.';
No rows affected (0.085 seconds)
0: jdbc:hive2://localhost:10000> describe database test1;
+----------+------------------------------------+----------------------------------------------------+-------------+-------------+-------------+
| db_name  |              comment               |                      location                      | owner_name  | owner_type  | parameters  |
+----------+------------------------------------+----------------------------------------------------+-------------+-------------+-------------+
| test1    | This db is for big data training.  | hdfs://localhost:9000/user/hive/warehouse/test1.db | train       | USER        |             |
+----------+------------------------------------+----------------------------------------------------+-------------+-------------+-------------+
1 row selected (0.115 seconds)
```

