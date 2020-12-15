import findspark
findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

lines = (spark
.readStream.format("socket")
.option("host", "localhost")
.option("port", 9999)
.load())

words = lines.select( F.explode(F.split(F.col("value"), "\\s+")).alias("word"))
counts = words.groupBy("word").count()
checkpointDir = "/user/train/wordCountCheckpoint"

streamingQuery = (counts
.writeStream
.format("console")
.outputMode("complete")
.trigger(processingTime="2 second")
.option("checkpointLocation", checkpointDir)
.start())

streamingQuery.awaitTermination()
