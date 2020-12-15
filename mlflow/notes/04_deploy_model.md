## Serve the model on port 5001 
(5000 is being listend by mlflow tracking server)
1. Go mlflow ui -> Experiments -> Model and get  model full path
hdfs://localhost:9000/user/train/mlflow/<id>/artifacts/model

2. Terminal-1: Serve the model
` mlflow models serve -m hdfs://localhost:9000/user/train/mlflow/94f01f30c7b947dbaf8f22a8407f9d1d/artifacts/model -h 0.0.0.0 -p 5001 --no-conda `

- Wait for the following output:
```
2020-11-29 07:39:13,725 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
2020/11/29 07:39:15 INFO mlflow.models.cli: Selected backend for flavor 'python_function'
2020/11/29 07:39:16 INFO mlflow.pyfunc.backend: === Running command 'gunicorn --timeout=60 -b 0.0.0.0:5001 -w 1 ${GUNICORN_CMD_ARGS} -- mlflow.pyfunc.scoring_server.wsgi:app'
[2020-11-29 07:39:17 +0300] [27232] [INFO] Starting gunicorn 20.0.4
[2020-11-29 07:39:17 +0300] [27232] [INFO] Listening at: http://0.0.0.0:5001 (27232)
[2020-11-29 07:39:17 +0300] [27232] [INFO] Using worker: sync
[2020-11-29 07:39:17 +0300] [27235] [INFO] Booting worker with pid: 27235
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
/home/train/venvspark/lib/python3.6/site-packages/pyspark/sql/context.py:77: DeprecationWarning: Deprecated in 3.0.0. Use SparkSession.builder.getOrCreate() instead.
  DeprecationWarning)
2020/11/29 07:39:38 INFO mlflow.spark: File '/tmp/tmpvpq8fmlg/sparkml' not found on DFS. Will attempt to upload the file.
2020/11/29 07:39:38 INFO mlflow.spark: Copied SparkML model to /tmp/mlflow/716f2081-f2d7-40d7-8eca-bb139c4a0c56
```
3. Terminal-2: make predictions
```
curl http://127.0.0.1:5001/invocations -H 'Content-Type: application/json' -d '{
    "columns": ["TV", "Radio", "Newspaper"],
    "data": [[97.5, 7.6, 7.2]]
}'
```
Expected output: ` [10.70547619047619] `

Multiple prediction
```
curl http://127.0.0.1:5001/invocations -H 'Content-Type: application/json' -d '{
    "columns": ["TV", "Radio", "Newspaper"],
    "data": [[230.1, 37.8, 69.2],[97.5, 7.6, 7.2]]
}'
```
Result ` [20.843874999999997, 10.70547619047619]  `

## Make predictions with Postman
1. On Virtualbox settings -> network forward 5000 and 5001 ports

2. On host machine open Postman

3. Create a new collection on left menu

4. Create a new tab clicking +

5. Select `POST` from dropdown and url will be `http://127.0.0.1:5001/invocations`  

6. From Headers Tab Add
Key -> Content-Type
value -> application/json

7. Body tab select raw radio button and JSON from dropdown

```
{
    "columns": ["TV", "Radio", "Newspaper"],
    "data": [[97.5, 7.6, 7.2],[230.1, 37.8, 69.2]]
}
```
8. Click Send

9. Expected result
```
[
    10.70547619047619,
    20.843874999999997
]
```

10. Terminal-1: Ctrl+C to stop deployment.

## Deploy registered model with the name and version/stage
- Export tracking URI
```
(venvspark) [train@localhost spark_advertsing_regression]$ export MLFLOW_TRACKING_URI=http://localhost:5000
(venvspark) [train@localhost spark_advertsing_regression]$ echo $MLFLOW_TRACKING_URI
http://localhost:5000
```
- Serve the model with name and version
```
(venvspark) [train@localhost spark_advertsing_regression]$ mlflow models serve -m "models:/spark-gbt-regressor/3" -h 0.0.0.0 -p 5001 --no-conda
```
wait until to see folllowing output
```
2020-11-29 08:15:25,497 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
2020/11/29 08:15:27 INFO mlflow.models.cli: Selected backend for flavor 'python_function'
2020/11/29 08:15:28 INFO mlflow.pyfunc.backend: === Running command 'gunicorn --timeout=60 -b 0.0.0.0:5001 -w 1 ${GUNICORN_CMD_ARGS} -- mlflow.pyfunc.scoring_server.wsgi:app'
[2020-11-29 08:15:29 +0300] [30271] [INFO] Starting gunicorn 20.0.4
[2020-11-29 08:15:29 +0300] [30271] [INFO] Listening at: http://0.0.0.0:5001 (30271)
[2020-11-29 08:15:29 +0300] [30271] [INFO] Using worker: sync
[2020-11-29 08:15:29 +0300] [30274] [INFO] Booting worker with pid: 30274
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
/home/train/venvspark/lib/python3.6/site-packages/pyspark/sql/context.py:77: DeprecationWarning: Deprecated in 3.0.0. Use SparkSession.builder.getOrCreate() instead.
  DeprecationWarning)
2020/11/29 08:15:49 INFO mlflow.spark: File '/tmp/tmpv9hj3c_0/sparkml' not found on DFS. Will attempt to upload the file.
2020/11/29 08:15:50 INFO mlflow.spark: Copied SparkML model to /tmp/mlflow/39ec2db5-4c64-434e-b744-fc97de750cab
```
- Terminal-2 make some redictions with curl
```
curl http://127.0.0.1:5001/invocations -H 'Content-Type: application/json' -d '{
    "columns": ["TV", "Radio", "Newspaper"],
    "data": [[97.5, 7.6, 7.2]]
}'
```
Expected output: ` [10.70547619047619] `

Multiple prediction
```
curl http://127.0.0.1:5001/invocations -H 'Content-Type: application/json' -d '{
    "columns": ["TV", "Radio", "Newspaper"],
    "data": [[230.1, 37.8, 69.2],[97.5, 7.6, 7.2]]
}'
```
Result ` [20.843874999999997, 10.70547619047619]  `




