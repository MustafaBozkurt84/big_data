import findspark
findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder
.appName("Write to Kafka")
.getOrCreate())

# spark.sparkContext.setLogLevel('ERROR')
checkpoint_dir = "hdfs://localhost:9000/user/train/write_to_kafka"


lines = (spark
.readStream
.format("kafka")
.option("kafka.bootstrap.servers", "localhost:9092")
.option("subscribe", "test1")
.load())


lines2 = lines.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

streamingQuery = (lines2
.writeStream
.format("kafka")
.option("kafka.bootstrap.servers", "localhost:9092")
.option("topic", "test2")
.outputMode("update")
.option("checkpointLocation", checkpoint_dir)
.start())



streamingQuery.awaitTermination()