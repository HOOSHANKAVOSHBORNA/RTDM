import asyncio
import websockets
from confluent_kafka import Producer, Consumer, KafkaException
import json

broker = 'localhost:9094'

producer_conf = {
    'bootstrap.servers': broker,
}

consumer_conf = {
    'bootstrap.servers': broker,
    'group.id': 'websocket-consumer',
    'auto.offset.reset': 'earliest'
}

producer = Producer(**producer_conf)

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

async def ws2kafka(websocket, data):
    print("handle")
    topic = data.get('topic')
    payload = data.get('payload')

    if topic and payload:
        # Produce the message to the Kafka topic
        producer.produce(topic, value=json_serializer(payload))
        producer.flush()
        await websocket.send(f"Message sent to Kafka topic {topic}")

async def kafka2ws(websocket, topic):
    print("send")
    consumer = Consumer(**consumer_conf)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    print(f"Reached end of partition {msg.partition()}\n")
                    break
                else:
                    raise KafkaException(msg.error())
            else:
                # Send the message to the WebSocket client
                await websocket.send(msg.value().decode())
    except websockets.exceptions.ConnectionClosedError:
        print("Connection with client closed.")
    finally:
        consumer.close()

async def websocket_handler(websocket, path):
    try:
        
        async for message in websocket:
        
            data = json.loads(message)
            await ws2kafka(websocket, data)
            await kafka2ws(websocket, "test1")
            
            
            
            
            
    except websockets.exceptions.ConnectionClosedError:
        print("WebSocket connection closed")
    except Exception as e:
        print(f"Error: {e}")

start_server = websockets.serve(websocket_handler, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

