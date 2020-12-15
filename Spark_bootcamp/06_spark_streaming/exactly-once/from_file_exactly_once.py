import findspark
findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.getOrCreate()

# spark.sparkContext.setLogLevel('ERROR')
checkpoint_dir = "hdfs://localhost:9000/user/train/exactly_once_guarantee"

lines = (spark
.readStream.format("text")
.option("maxFilesPerTrigger", 1)
.load("file:///home/train/data-generator/output"))


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