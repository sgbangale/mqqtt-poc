# MQTT Publisher and Subscriber using `gmqtt`

This repository demonstrates a simple MQTT publisher and subscriber using the `gmqtt` Python library. The publisher sends a message to a topic, and the subscriber listens for messages on that topic.

## Requirements

- Python 3.7+
- Docker
- `gmqtt` library

## Getting Started

### Step 1: Install Python Dependencies

First, install the required Python library `gmqtt` using `pip`:

```bash
pip install gmqtt
```

### Step 2: Run the MQTT Broker (EMQX) using Docker

We will use the EMQX broker for MQTT message handling. You can spin up the broker using Docker with the following command:

```bash
docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 18083:18083 emqx/emqx
```

- Port `1883`: MQTT protocol port.
- Port `8083`: WebSocket port (optional).
- Port `18083`: EMQX dashboard (optional).

You can access the EMQX dashboard at `http://localhost:18083`. The default login credentials are:
- Username: `admin`
- Password: `public`

### Step 3: Running the Subscriber

In one terminal, run the subscriber script to listen for messages on the `test/topic`:

```bash
python subscriber.py
```

This will connect to the EMQX broker and subscribe to the `test/topic`. The subscriber will print any messages it receives.

### Step 4: Running the Publisher

In another terminal, run the publisher script to send a message to the `test/topic`:

```bash
python publisher.py
```

This will connect to the EMQX broker and publish a message (`Hello from gmqtt!`) to the `test/topic`.

### Step 5: Verify Message Reception

Once the publisher sends the message, you should see it printed by the subscriber terminal as follows:

```bash
Message received on test/topic: Hello from gmqtt!
```