1. Generally we load data to hive from hdfs bu it is possible to load from local but not practical. It is against to big data concepts
there are tens of servers if not hundreds, and data splitted out these server which one which local?

2. Load data from hdfs

2.1. Create a table that suits data in hdfs but it is better to see data first
```
[train@localhost ~]$ hdfs dfs -head /user/train/datasets/Advertising.csv
ID,TV,Radio,Newspaper,Sales
1,230.1,37.8,69.2,22.1
2,44.5,39.3,45.1,10.4
3,17.2,45.9,69.3,9.3
4,151.5,41.3,58.5,18.5
..
..
```
2.2. Now create table. Notice there is header in the data so we specify it in create statement table properties     
```
[train@localhost ~]$ beeline -u jdbc:hive2://localhost:10000

# close warnings
jdbc:hive2://localhost:10000> set hive.server2.logging.operation.level=NONE;

# select test1 database
0: jdbc:hive2://localhost:10000> use test1;

# select test1 database
0: jdbc:hive2://localhost:10000> drop advertising;

# create table
0: jdbc:hive2://localhost:10000> create table if not exists advertising
. . . . . . . . . . . . . . . .>  (id int, tv float, radio float, newspaper float, sales float)
. . . . . . . . . . . . . . . .>  row format delimited
. . . . . . . . . . . . . . . .> fields terminated by ','
. . . . . . . . . . . . . . . .> lines terminated by '\n'
. . . . . . . . . . . . . . . .> stored as textfile
. . . . . . . . . . . . . . . .> tblproperties('skip.header.line.count'='1');
No rows affected (0.835 seconds)


# inspect table
0: jdbc:hive2://localhost:10000> describe advertising;
+------------+------------+----------+
|  col_name  | data_type  | comment  |
+------------+------------+----------+
| id         | int        |          |
| tv         | float      |          |
| radio      | float      |          |
| newspaper  | float      |          |
| sales      | float      |          |
+------------+------------+----------+
5 rows selected (0.212 seconds)

# select if there is any record
0: jdbc:hive2://localhost:10000> select * from advertising;
+-----------------+-----------------+--------------------+------------------------+--------------------+
| advertising.id  | advertising.tv  | advertising.radio  | advertising.newspaper  | advertising.sales  |
+-----------------+-----------------+--------------------+------------------------+--------------------+
+-----------------+-----------------+--------------------+------------------------+--------------------+
```

2.3. Load data to hive table
```
0: jdbc:hive2://localhost:10000> load data inpath '/user/train/datasets/Advertising.csv' into table advertising;
No rows affected (0.487 seconds)
```
2.4. See the data
```
0: jdbc:hive2://localhost:10000> select * from advertising limit 3;
+-----------------+-----------------+--------------------+------------------------+--------------------+
| advertising.id  | advertising.tv  | advertising.radio  | advertising.newspaper  | advertising.sales  |
+-----------------+-----------------+--------------------+------------------------+--------------------+
| 1               | 230.1           | 37.8               | 69.2                   | 22.1               |
| 2               | 44.5            | 39.3               | 45.1                   | 10.4               |
| 3               | 17.2            | 45.9               | 69.3                   | 9.3                |
+-----------------+-----------------+--------------------+------------------------+--------------------+
3 rows selected (0.393 seconds)
```

2.5. Check data in hdfs  
`[train@localhost ~]$ hdfs dfs -ls /user/train/datasets | grep Advertising`  
You will see the data has gone where is it now?  
It is in the default hive warehouse directory. Let's check it.
```
[train@localhost ~]$ hdfs dfs -ls /user/hive/warehouse/test1.db/advertising
Found 1 items
-rw-r--r--   1 train supergroup       4556 2020-09-16 14:58 /user/hive/warehouse/test1.db/advertising/Advertising.csv
```

2.6. If you see the result like this
```
0: jdbc:hive2://localhost:10000> select * from advertising limit 10;
+-----------------+-----------------+--------------------+------------------------+--------------------+
| advertising.id  | advertising.tv  | advertising.radio  | advertising.newspaper  | advertising.sales  |
+-----------------+-----------------+--------------------+------------------------+--------------------+
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
| NULL            | NULL            | NULL               | NULL                   | NULL               |
+-----------------+-----------------+--------------------+------------------------+--------------------+
10 rows selected (0.253 seconds)
```
It is possibly due to schema data conflict. Check your create table and properties.
If you try second time you have to -put your data to hdfs again because it has already gone.


2.8. load overwrite mode  
put data to hdfs `[train@localhost big_data]$ hdfs dfs -put ~/datasets/Advertising.csv /user/train/datasets`

2.9. Load again  

```
# cout the curent records
0: jdbc:hive2://localhost:10000> select count(1) from advertising;
+------+
| _c0  |
+------+
| 200  |
+------+
1 row selected (53.026 seconds)

# load the same data overwrite
0: jdbc:hive2://localhost:10000> load data inpath '/user/train/datasets/Advertising.csv' overwrite into table advertising;


0: jdbc:hive2://localhost:10000> select count(1) from advertising;
+------+
| _c0  |
+------+
| 200  |
+------+
1 row selected (38.973 seconds)

```
See there is still 200 records.

2.10. put data hdfs and try again but this time not overwrite
`[train@localhost big_data]$ hdfs dfs -put ~/datasets/Advertising.csv /user/train/datasets`

```
0: jdbc:hive2://localhost:10000> load data inpath '/user/train/datasets/Advertising.csv' into table advertising;
No rows affected (0.269 seconds)

0: jdbc:hive2://localhost:10000> select count(1) from advertising;
+------+
| _c0  |
+------+
| 400  |
+------+
1 row selected (40.15 seconds)
```

**into appends, overwrite into overwrites.**  

3. Load data from local
```
0: jdbc:hive2://localhost:10000> load data local inpath '/home/train/datasets/Advertising.csv' into table advertising;
No rows affected (0.644 seconds)

0: jdbc:hive2://localhost:10000> select count(1) from advertising;
+------+
| _c0  |
+------+
| 600  |
+------+
1 row selected (38.063 seconds)
```