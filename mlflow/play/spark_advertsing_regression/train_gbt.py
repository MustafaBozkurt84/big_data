from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession, functions as F
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.regression import GBTRegressor
from pyspark.ml import Pipeline
import mlflow
import mlflow.spark
import pandas as pd
import os

import findspark
findspark.init("/opt/manual/spark/")

spark = (SparkSession.builder
         .appName("Spark Advertising Train Model")
         .master("yarn")
         .getOrCreate())

df = (spark
      .read
      .format("csv")
      .option("inferSchema",True)
      .option("header", True)
      .option("sep",",")
      .load("hdfs://localhost:9000/user/train/datasets/Advertising.csv"))

df.show(3)

train_df, test_df = df.randomSplit([.8, .2], seed=142)
assembler = VectorAssembler(handleInvalid='skip',
                            inputCols=['TV','Radio','Newspaper'],
                            outputCol='features')


estimator =  GBTRegressor(featuresCol='features',
                                  labelCol='Sales',
                                  predictionCol='prediction')

pipeline_obj = Pipeline(stages=[assembler, estimator])

mlflow.set_tracking_uri('http://localhost:5000/')
print("mlflow tracking_uri: " + mlflow.tracking.get_tracking_uri())

mlflow.set_experiment("Advertising Regression Online Lesson")

with mlflow.start_run(run_name="spark-advertising-gbt-regressor") as run:
    # Log params:
    mlflow.log_param("min_info_gain", estimator.getMinInfoGain())
    mlflow.log_param("max_depth", estimator.getMaxDepth())
    mlflow.log_param("max_bins", estimator.getMaxBins())
    mlflow.log_param("step_size", estimator.getStepSize())

    # Log the model while training
    pipelineModel = pipeline_obj.fit(train_df)
    mlflow.spark.log_model(pipelineModel, "model")

    # Log metrics: RMSE and R2
    predDF = pipelineModel.transform(test_df)
    regressionEvaluator = RegressionEvaluator(predictionCol="prediction", labelCol="Sales")
    rmse = regressionEvaluator.setMetricName("rmse").evaluate(predDF)
    r2 = regressionEvaluator.setMetricName("r2").evaluate(predDF)
    mlflow.log_metrics({"rmse": rmse, "r2": r2})

    # Log model and register as version 1
    mlflow.spark.log_model(
        spark_model=pipelineModel,
        artifact_path="spark-gbt-regressor",
        registered_model_name="spark-gbt-regressor")
		
    # After run you can go ui and see the model http://localhost:5000/#/models
    # Log artifact: feature importance scores
    rfModel = pipelineModel.stages[-1]
    pandasDF = (pd.DataFrame(list(zip(assembler.getInputCols(), rfModel.featureImportances)),
                             columns=["feature", "importance"]).sort_values(by="importance", ascending=False))

    # First write to local filesystem, then tell MLflow where to find that file
    pandasDF.to_csv("advertising-feature-importance.csv", index=False)
    mlflow.log_artifact("advertising-feature-importance.csv")

# Since we used with block start_run we don't need to explicitly call end_run
# mlflow.end_run(status='FINISHED')