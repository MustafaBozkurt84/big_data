1. Create table with properties
```
0: jdbc:hive2://localhost:10000> 0: jdbc:hive2://localhost:10000> create table if not exists mytable
. . . . . . . . . . . . . . . .> (id int, username string, email array<string>)
. . . . . . . . . . . . . . . .>  row format delimited
. . . . . . . . . . . . . . . .> fields terminated by ','
. . . . . . . . . . . . . . . .> collection items terminated by ':'
. . . . . . . . . . . . . . . .>  lines terminated by '\n'
. . . . . . . . . . . . . . . .> stored as textfile;
No rows affected (0.154 seconds)
```

2. insert a record with values  
`0: jdbc:hive2://localhost:10000> insert into mytable values(2, "testuser2", array("testuser2@example.com")); `

3. insert a record with SELECT  
`0: jdbc:hive2://localhost:10000> insert into mytable SELECT 1, "testuser1", array("testuser1@example.com"); `

4. insert a record with multiple array elements  
`0: jdbc:hive2://localhost:10000> insert into table mytable values(3, 'testuser3', array('testuser3@example.com:testuser3@gmail.com')); `

5. insert multiple records
```
0: jdbc:hive2://localhost:10000> insert into table mytable values (4, 'testuser4', array('testuser4@example.com:testuser4@gmail.com')),  (5, 'testuser5', array('testuser5@example.com:testuser5@gmail.com'));
```

6. See inserted records
```
0: jdbc:hive2://localhost:10000> select * from mytable;
+-------------+-------------------+--------------------------------------------------+
| mytable.id  | mytable.username  |                  mytable.email                   |
+-------------+-------------------+--------------------------------------------------+
| 1           | testuser1         | ["testuser1@example.com"]                        |
| 2           | testuser2         | ["testuser2@example.com"]                        |
| 3           | testuser3         | ["testuser3@example.com","testuser3@gmail.com"]  |
| 4           | testuser4         | ["testuser4@example.com","testuser4@gmail.com"]  |
| 5           | testuser5         | ["testuser5@example.com","testuser5@gmail.com"]  |
+-------------+-------------------+--------------------------------------------------+
5 rows selected (0.248 seconds)
```
