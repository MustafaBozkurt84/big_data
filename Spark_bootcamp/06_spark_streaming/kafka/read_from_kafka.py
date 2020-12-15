import findspark
findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

spark = (SparkSession.builder
.appName("Read From Kafka")
.getOrCreate())

# spark.sparkContext.setLogLevel('ERROR')
checkpoint_dir = "hdfs://localhost:9000/user/train/read_from_kafka"


lines = (spark
.readStream
.format("kafka")
.option("kafka.bootstrap.servers", "localhost:9092")
.option("subscribe", "test1")
.load())


# lines2 = lines.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "topic", "partition", "offset", "timestamp")





streamingQuery = (lines
.writeStream
.format("console")
.outputMode("append")
.trigger(processingTime="1 second")
.option("checkpointLocation", checkpoint_dir)
.option("numRows",4)
.option("truncate",False)
.start())



streamingQuery.awaitTermination()