1. Select test1 database
`use test1;`

2. Create simple table with default properties
```
0: jdbc:hive2://localhost:10000> create table if not exists mytable(id int, user_name string, email string);
No rows affected (0.25 seconds)

0: jdbc:hive2://localhost:10000> show tables;
+-----------+
| tab_name  |
+-----------+
| mytable   |
+-----------+
1 row selected (0.097 seconds)
```

3. Describe table
```
0: jdbc:hive2://localhost:10000> describe mytable;
+------------+------------+----------+
|  col_name  | data_type  | comment  |
+------------+------------+----------+
| id         | int        |          |
| user_name  | string     |          |
| email      | string     |          |
+------------+------------+----------+
3 rows selected (0.141 seconds)
```

4. More information for table
```
0: jdbc:hive2://localhost:10000> describe formatted  mytable;
+-------------------------------+----------------------------------------------------+----------------------------------------------------+
|           col_name            |                     data_type                      |                      comment                       |
+-------------------------------+----------------------------------------------------+----------------------------------------------------+
| # col_name                    | data_type                                          | comment                                            |
| id                            | int                                                |                                                    |
| user_name                     | string                                             |                                                    |
| email                         | string                                             |                                                    |
|                               | NULL                                               | NULL                                               |
| # Detailed Table Information  | NULL                                               | NULL                                               |
| Database:                     | test1                                              | NULL                                               |
| OwnerType:                    | USER                                               | NULL                                               |
| Owner:                        | train                                              | NULL                                               |
| CreateTime:                   | Wed Sep 16 12:13:14 TRT 2020                       | NULL                                               |
| LastAccessTime:               | UNKNOWN                                            | NULL                                               |
| Retention:                    | 0                                                  | NULL                                               |
| Location:                     | hdfs://localhost:9000/user/hive/warehouse/test1.db/mytable | NULL                                               |
| Table Type:                   | MANAGED_TABLE                                      | NULL                                               |
| Table Parameters:             | NULL                                               | NULL                                               |
|                               | COLUMN_STATS_ACCURATE                              | {\"BASIC_STATS\":\"true\",\"COLUMN_STATS\":{\"email\":\"true\",\"id\":\"true\",\"user_name\":\"true\"}} |
|                               | bucketing_version                                  | 2                                                  |
|                               | numFiles                                           | 0                                                  |
|                               | numRows                                            | 0                                                  |
|                               | rawDataSize                                        | 0                                                  |
|                               | totalSize                                          | 0                                                  |
|                               | transient_lastDdlTime                              | 1600247594                                         |
|                               | NULL                                               | NULL                                               |
| # Storage Information         | NULL                                               | NULL                                               |
| SerDe Library:                | org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe | NULL                                               |
| InputFormat:                  | org.apache.hadoop.mapred.TextInputFormat           | NULL                                               |
| OutputFormat:                 | org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat | NULL                                               |
| Compressed:                   | No                                                 | NULL                                               |
| Num Buckets:                  | -1                                                 | NULL                                               |
| Bucket Columns:               | []                                                 | NULL                                               |
| Sort Columns:                 | []                                                 | NULL                                               |
| Storage Desc Params:          | NULL                                               | NULL                                               |
|                               | serialization.format                               | 1                                                  |
+-------------------------------+----------------------------------------------------+----------------------------------------------------+
33 rows selected (0.209 seconds)
```
5. drop table ` drop table mytable;`



6. Comment while creating table
`0: jdbc:hive2://localhost:10000> create table if not exists mytable(id int, user_name string, email string) comment 'This table is for test';`

7. See comment in output of `describe formatted mytable;`

8. Create table with properties
```
0: jdbc:hive2://localhost:10000> create table if not exists mytable (id int, username string, email array<string>) row format delimited fields terminated by ',' collection items terminated by ':' lines terminated by '\n' stored as textfile;
No rows affected (0.154 seconds)
```

9. generate create script from existing table
```
0: jdbc:hive2://localhost:10000> show create table mytable;
+----------------------------------------------------+
|                   createtab_stmt                   |
+----------------------------------------------------+
| CREATE TABLE `mytable`(                            |
|   `id` int,                                        |
|   `username` string,                               |
|   `email` array<string>)                           |
| ROW FORMAT SERDE                                   |
|   'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'  |
| WITH SERDEPROPERTIES (                             |
|   'collection.delim'=':',                          |
|   'field.delim'=',',                               |
|   'line.delim'='\n',                               |
|   'serialization.format'=',')                      |
| STORED AS INPUTFORMAT                              |
|   'org.apache.hadoop.mapred.TextInputFormat'       |
| OUTPUTFORMAT                                       |
|   'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat' |
| LOCATION                                           |
|   'hdfs://localhost:9000/user/hive/warehouse/test1.db/mytable' |
| TBLPROPERTIES (                                    |
|   'bucketing_version'='2',                         |
|   'transient_lastDdlTime'='1600272299')            |
+----------------------------------------------------+
20 rows selected (0.264 seconds)
```
