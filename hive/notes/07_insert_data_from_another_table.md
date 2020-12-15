## create table using another table
```
0: jdbc:hive2://localhost:10000> create table advertising_sales_gt_20 as select * from advertising where sales > 20;
No rows affected (30.624 seconds)
```
## Check the result
count new table
```
0: jdbc:hive2://localhost:10000> select count(1) from advertising_sales_gt_20;
+------+
| _c0  |
+------+
| 31   |
+------+
```

## Append new data (insert into)
```
0: jdbc:hive2://localhost:10000> insert into table advertising_sales_gt_20 select * from advertising where sales > 20;
No rows affected (42.036 seconds)


0: jdbc:hive2://localhost:10000> select count(1) from advertising_sales_gt_20;
+------+
| _c0  |
+------+
| 62   |
+------+
1 row selected (0.255 seconds)

```

## overwrite data on existing table with select (insert overwrite)

```
0: jdbc:hive2://localhost:10000> insert overwrite table advertising_sales_gt_20 select * from advertising where sales > 20;
No rows affected (41.091 seconds)

0: jdbc:hive2://localhost:10000> select count(1) from advertising_sales_gt_20;
+------+
| _c0  |
+------+
| 31   |
+------+
1 row selected (0.221 seconds)

```
if you user insert in place of overwrite the data will be appended.