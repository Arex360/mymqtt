import paho.mqtt.client as mqtt
import base64
import requests
# MQTT Settings
MQTT_BROKER = "152.67.19.152"  # Change this if your broker is on a different machine
MQTT_PORT = 1883
MQTT_TOPIC = "client9"

# Callback when a message is received
def on_messageStart(client, userdata, msg):
    if "_0_" in msg.payload:
        print("its start")
    print(len(msg.payload))


# Create MQTT client
client = mqtt.Client()
client.on_message = on_messageStart 
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_forever()

