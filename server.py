import paho.mqtt.client as mqtt
import base64
import requests
# MQTT Settings
MQTT_BROKER = "152.67.19.152"  # Change this if your broker is on a different machine
MQTT_PORT = 1883
MQTT_TOPIC = "client9"

# Callback when a message is received
def on_messageStart(client, userdata, msg):
    a = str(msg.payload)
    if "_0_" in a:
        print("its start")
    if "_1_" in a:
        print("its mids")
    if "_2_" in a:
        print("its end")
    print(len(a))


# Create MQTT client
client = mqtt.Client()
client.on_message = on_messageStart 
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_forever()

