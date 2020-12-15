import time, sys, os
from pathlib import Path
from datetime import datetime
import argparse
import findspark
findspark.init("/opt/manual/spark")

from pyspark.sql import SparkSession, functions as F

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input", required=True, type=str, default='hdfs://localhost:9000/user/train/datasets/market5mil_snappyparquet',
                    help="Source file path.")

ap.add_argument("-f", "--format", required=True, type=str, default='csv',
                    help="Source file type. Csv, parquet, orc etc.")

ap.add_argument("-head", "--header", required=False, type=bool, default=None,
                    help="True if the first line is heade in csv or text source.")

ap.add_argument("-s", "--sep", required=False, type=str, default=',',
                    help="Seperator of columns, fields.")

ap.add_argument("-sch", "--inferSchema", required=False, type=bool, default=None,
                    help="If True spark infers field type while reading.")

ap.add_argument("-c", "--compression", required=False, type=str, default=None,
                    help="File compression types gzip, lzo, snappy")
                    
ap.add_argument("-name", "--appName", required=False, type=str, default="Default App",
                    help="Spark Application name")

args = vars(ap.parse_args())

input=args['input']
format=args['format']
header=args['header']
sep=args['sep']
inferSchema=args['inferSchema']
compression=args['compression']
appName=args['appName']

# create a SparkSession
spark = SparkSession.builder.appName(appName).getOrCreate()

df = spark.read.format(format) \
.option("inferSchema", inferSchema) \
.option("header",header) \
.option("sep", sep) \
.load(input)

df.select(df.columns[:5]).show()

spark.stop()
