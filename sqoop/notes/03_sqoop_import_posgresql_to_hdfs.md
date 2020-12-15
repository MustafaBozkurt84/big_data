1. Create and hdfs folder for sqoop_import  
`  [train@localhost play]$ hdfs dfs -mkdir /user/train/output_data/sqoop_import  `

2. Sqoop import
```
sqoop import --connect jdbc:postgresql://localhost:5432/traindb  \
--driver org.postgresql.Driver \
--username train --password Ankara06 \
--table churn --m 4 --split-by rownumber --target-dir /user/train/output_data/sqoop_import/churn
```

3. See the results from command line or Namenode UI
```
[train@localhost play]$ hdfs dfs -ls /user/train/output_data/sqoop_import/churn
Found 5 items
-rw-r--r--   1 train supergroup          0 2020-09-18 06:26 /user/train/output_data/sqoop_import/churn/_SUCCESS
-rw-r--r--   1 train supergroup     169844 2020-09-18 06:26 /user/train/output_data/sqoop_import/churn/part-m-00000
-rw-r--r--   1 train supergroup     171064 2020-09-18 06:26 /user/train/output_data/sqoop_import/churn/part-m-00001
-rw-r--r--   1 train supergroup     170654 2020-09-18 06:26 /user/train/output_data/sqoop_import/churn/part-m-00002
-rw-r--r--   1 train supergroup     170774 2020-09-18 06:26 /user/train/output_data/sqoop_import/churn/part-m-00003
```

4. read importes file
```
[train@localhost play]$ hdfs dfs -head  /user/train/output_data/sqoop_import/churn/part-m-00000
1,15634602,Hargrave,619,France,Female,42,2,0.0,1,1,1,101348.88,1
2,15647311,Hill,608,Spain,Female,41,1,83807.86,1,0,1,112542.58,0
3,15619304,Onio,502,France,Female,42,8,159660.8,3,1,0,113931.57,1
4,15701354,Boni,699,France,Female,39,1,0.0,2,0,0,93826.63,0
5,15737888,Mitchell,850,Spain,Female,43,2,125510.82,1,1,1,79084.1,0
6,15574012,Chu,645,Spain,Male,44,8,113755.78,2,1,0,149756.71,1
7,15592531,Bartlett,822,France,Male,50,7,0.0,2,1,1,10062.8,0
8,15656148,Obinna,376,Germany,Female,29,4,115046.74,4,1,0,119346.88,1
9,15792365,He,501,France,Male,44,4,142051.07,2,0,1,74940.5,0
10,15592389,H?,684,France,Male,27,2,134603.88,1,1,1,71725.73,0
11,15767821,Bearce,528,France,Male,31,6,102016.72,2,0,0,80181.12,0
12,15737173,Andrews,497,Spain,Male,24,3,0.0,2,1,0,76390.01,0
13,15632264,Kay,476,France,Female,34,10,0.0,2,1,0,26260.98,0
14,15691483,Chin,549,France,Female,25,5,0.0,2,0,0,190857.79,0
15,15600882,Scott,635,Spain,Female,35,7,0.0,2,1,1,65951.65,0
16,15643966,Goforth,616,Germany,Male,45,3,143129.41,2,0,1,64327.26,0
```

5. To overwrite existing directory just add `--delete-target-dir` before `--target-dir`


