1. Connect hive shell
`hive`

2. list databases
```
hive> show databases;
OK
bookstore
default
train
Time taken: 2.236 seconds, Fetched: 3 row(s)
```

3. Select a database and list tables in it
```
hive> use bookstore;
OK
Time taken: 0.059 seconds
hive> show tables;
OK
books
Time taken: 0.059 seconds, Fetched: 1 row(s)
```

4. Sample query
```
hive> select book_name from books;
OK
Madam Bovary (Ciltli)
Mai ve Siyah (Eleştirel Basım)
Nutuk
Devlet
Time taken: 3.857 seconds, Fetched: 4 row(s)
```

5. Exit from hive-shell
`exit;`

