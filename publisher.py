import asyncio
from gmqtt import Client as MQTTClient

# MQTT Broker details
broker = "localhost"
port = 1883
topic = "test/topic"

# Callback when the client connects
def on_connect(client, flags, rc, properties):
    print('Connected to broker')
    # Publish a message once connected
    client.publish(topic, "Hello from gmqtt!", qos=0)

async def run():
    client = MQTTClient("publisher-client")

    # Attach the callback function (regular function)
    client.on_connect = on_connect

    # Connect to the broker
    await client.connect(broker, port)

    # Keep the script alive for a while to ensure message is published
    await asyncio.sleep(2)

    # Disconnect after publishing
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(run())