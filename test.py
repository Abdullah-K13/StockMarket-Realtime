import pandas as pd
from confluent_kafka import Producer, Consumer
import json
import s3fs


df = pd.read_csv('data/indexProcessed.csv')


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key= 'AKIA57VDLVSDNWWZ6ZMV',
                               secret='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',
                               client_kwargs={'region_name': 'us-east-1'})
        return s3
    except Exception as e:
        print(e)

# Example producer
def producer():

    conf = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(conf)
    print('i am in producer')

    producer.flush()
    # while True:
    #     dict_stock = df.sample(1).to_dict(orient="records")[0] 
        # print(dict_stock)
        # message = json.dumps(dict_stock).encode('utf-8')
        # producer.produce('demo_test', value=message)
         
  

def consumer():
    print('hello')
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(conf)
    consumer.subscribe(['demo_test'])
    s3 = connect_to_s3()



    # for count, i in enumerate(consumer):
    #     with s3.open("s3://stockmarket-realtime/stock_market_{}.json".format(count), 'w') as file:
    #         json.dump(i.value, file)

    # while True:
    #     msg = consumer.poll(timeout=1.0)
    #     if msg is None:
    #         continue
    #     if msg.error():
    #         print('Consumer error: {}'.format(msg.error()))
    #         continue
    #     print('Received message: {}'.format(msg.value().decode('utf-8')))


    try:
        count = 0
        while True:
            # Poll for messages from Kafka
            msg = consumer.poll(1.0)  # Timeout of 1 second

            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            # Decode the message value
            message_value = msg.value().decode('utf-8')

            # Write the message to an S3 file
            # s3_path = f"s3://stockmarket-realtime/stock_market_{count}.json"
            # with s3.open(s3_path, 'w') as file:
            #     json.dump(message_value, file)

            print(f"Message {count} written to ")
            # print(message_value)

            count += 1

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


#producer()
consumer()

# print(df.head())
