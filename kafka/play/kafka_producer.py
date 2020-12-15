# Import libs
from kafka import KafkaProducer

# Create a producer object
# Ip can be different in your case
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for key in range(100):
    producer.send('topic1', key=str(key).encode(),
                  value=b'Python producer msg')

producer.flush()

# Before run open three consumer from three different terminal under same group.