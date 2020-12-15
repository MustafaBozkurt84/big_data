1. Download dataset to load postgresql  
` [train@localhost play]$ wget https://raw.githubusercontent.com/erkansirin78/datasets/master/Churn_Modelling.csv -P ~/datasets/ `

2. On DBeaver create a table
```
create table if not exists churn(RowNumber int,
CustomerId int,
Surname VARCHAR(50),
CreditScore int,
Geography VARCHAR(50),
Gender VARCHAR(10),
Age SMALLINT,
Tenure SMALLINT,
Balance float8,
NumOfProducts SMALLINT,
HasCrCard SMALLINT,
IsActiveMember SMALLINT,
EstimatedSalary float8,
Exited SMALLINT);
```

3. load csv to postgresql table
```
[train@localhost play]$ psql -d traindb -c "\copy churn FROM '/home/train/datasets/Churn_Modelling.csv' DELIMITERS ',' CSV HEADER;"
COPY 10000
```

```
[train@localhost play]$ psql -d traindb -c "select rownumber, geography, gender, balance from churn limit 5;"
 rownumber | geography | gender |  balance
-----------+-----------+--------+-----------
         1 | France    | Female |         0
         2 | Spain     | Female |  83807.86
         3 | France    | Female |  159660.8
         4 | France    | Female |         0
         5 | Spain     | Female | 125510.82
(5 rows)
```


