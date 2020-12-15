from pyspark.sql import SparkSession, functions as F
# Load saved model with MLflow
import mlflow.spark
import os

os.environ['MLFLOW_TRACKING_URI'] = 'http://localhost:5000/'
os.environ['PYSPARK_PYTHON'] = 'python3'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python3'
# Generate predictions
spark = (SparkSession.builder
         .appName("Spark Advertising Train Model")
         .master("yarn")
         .getOrCreate())

inputDF = (spark
      .read
      .format("csv")
      .option("inferSchema",True)
      .option("header", True)
      .option("sep",",")
      .load("hdfs://localhost:9000/user/train/datasets/Advertising.csv"))


import mlflow.pyfunc

data = inputDF.select("TV","Radio","Newspaper").limit(5).toPandas()
# You can leanr model name from http://localhost:5000/#/models
model_name = "spark-random-forest-reg-model"
model_version = 3

model = mlflow.pyfunc.load_model(
    model_uri=f"models:/{model_name}/{model_version}"
)
# data should be pandas dataframe
print(model.predict(data=data))
# Expected output
# [21.554416629994716, 11.217042979152959, 12.242694120291947, 18.38443154761905, 13.517194939980039]
