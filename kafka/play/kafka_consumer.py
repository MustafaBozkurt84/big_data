# Import libs
from kafka import KafkaConsumer

# Create consumer object
# Consume earliest messages,
# If there is no new message in 10 secondsstop consuming.
consumer = KafkaConsumer('topic1', # topic
                        group_id='group1',
                         # consume earliest available messages, for latest 'latest'
                         auto_offset_reset='earliest',
                         # don't commit offsets
                         enable_auto_commit=False,
                         # stop iteration if no message after 10 secs
                         consumer_timeout_ms=10000,
                         # kafka servers and port
                         bootstrap_servers=['localhost:9092'])

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value.decode('utf-8')))