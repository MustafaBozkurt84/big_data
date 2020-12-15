import findspark

findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("File Source CSV Stateless").getOrCreate()

spark.sparkContext.setLogLevel('ERROR')

iris_schema = "row_id int, SepalLengthCm float, SepalWidthCm float, PetalLengthCm float, PetalWidthCm float, " \
              "Species string, time timestamp "

lines = (spark
         .readStream.format("csv")
         .schema(iris_schema)
         .option("header", False)
         .load("file:///home/train/data-generator/output"))

# grouped_by_species = lines.select( F.explode(F.split(F.col("value"), "\\s+")).alias("word"))
# counts = words.groupBy("word").count()
checkpointDir = "/user/train/wordCountCheckpoint"

streamingQuery = (lines
                  .writeStream
                  .format("console")
                  .outputMode("append")
                  .trigger(processingTime="1 second")
                  .option("numRows", 4)
                  .option("truncate", False)
                  .start())

# .option("checkpointLocation", checkpointDir)
streamingQuery.awaitTermination()
