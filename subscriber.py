import asyncio
from gmqtt import Client as MQTTClient

# MQTT Broker details
broker = "localhost"
port = 1883
topic = "test/topic"

# Callback when the client connects
def on_connect(client, flags, rc, properties):
    print('Connected to broker')
    # Subscribe to the topic after connecting
    client.subscribe(topic, qos=0)

# Callback when a message is received
def on_message(client, topic, payload, qos, properties):
    print(f"Message received on {topic}: {payload.decode()}")

async def run():
    client = MQTTClient("subscriber-client")

    # Attach the callback functions (regular functions)
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the broker
    await client.connect(broker, port)

    # Run forever to process messages
    await asyncio.Future()  # Block forever

if __name__ == "__main__":
    asyncio.run(run())