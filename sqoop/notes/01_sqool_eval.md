1. Test your rdbms (postgresql) connection with sqoop eval
```
[train@localhost ~]$ sqoop eval \
> --connect jdbc:postgresql://localhost:5432/traindb \
> --driver org.postgresql.Driver \
> --username train --password Ankara06 \
> --query "select count(1) from books"
```

2. Where is the postgresql driver?
```
[train@localhost play]$ ll /opt/manual/sqoop/lib/ | grep postgresql
-rw-rw-r--. 1 train train  932808 Jul 22 06:02 postgresql-42.2.14.jar
```
The driver must be here.