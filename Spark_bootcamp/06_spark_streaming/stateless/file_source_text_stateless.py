import findspark
findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.getOrCreate()

spark.sparkContext.setLogLevel('ERROR')


lines = (spark
.readStream.format("text")
.option("cleanSource", "DELETE")
.load("file:///home/train/data-generator/output"))

lines2 = lines.select(F.split(F.col("value"), ","))

streamingQuery = (lines2
.writeStream
.format("console")
.outputMode("append")
.trigger(processingTime="1 second")
.option("numRows",4)
.option("truncate",False)
.start())


#.option("checkpointLocation", checkpointDir)
streamingQuery.awaitTermination()