import pandas as pd
import pyspark.pandas as ps
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

pandas_df = pd.read_json('tenth_scrape.json')

