# Import libs
from kafka import KafkaProducer
import pandas as pd
import time

# Create a producer object
# Ip can be different in your case
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


# Read csv file and quick overview

df = pd.read_csv("~/datasets/Advertising.csv")
print(df.head())
'''
   ID     TV  Radio  Newspaper  Sales
0   1  230.1   37.8       69.2   22.1
1   2   44.5   39.3       45.1   10.4
2   3   17.2   45.9       69.3    9.3
3   4  151.5   41.3       58.5   18.5
4   5  180.8   10.8       58.4   12.9
'''

# Null check
print(df.isnull().sum())
'''
ID           0
TV           0
Radio        0
Newspaper    0
Sales        0
dtype: int64
'''

# Put columns (including key column) to produce in a single columns named value
x = df.to_string(header=False,
                  index=False,
                  index_names=False).split('\n')
vals = [','.join(ele.split()) for ele in x]

df['value'] = vals

print(df.head())
'''
   ID     TV  Radio  Newspaper  Sales                   value
0   1  230.1   37.8       69.2   22.1  1,230.1,37.8,69.2,22.1
1   2   44.5   39.3       45.1   10.4   2,44.5,39.3,45.1,10.4
2   3   17.2   45.9       69.3    9.3    3,17.2,45.9,69.3,9.3
3   4  151.5   41.3       58.5   18.5  4,151.5,41.3,58.5,18.5
4   5  180.8   10.8       58.4   12.9  5,180.8,10.8,58.4,12.9
'''

# Iterate through dataframe and produce it
for index, row in df.iterrows():
    time.sleep(0.1)
    producer.send('topic1', key=str(row[0]).encode(), value=row[-1].encode())

# Observe results from three console consumer under group1