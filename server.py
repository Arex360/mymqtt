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
        a = a.replace("_0_","")
        myobj = {'base64': a}
        requests.post(f'http://localhost:5000/postImagePart/{msg.topic}/0',myobj)
    if "_1_" in a:
        print("its mids")
        a = a.replace("_1_","")
        myobj = {'base64': a}
        requests.post(f'http://localhost:5000/postImagePart/{msg.topic}/1',myobj)
    if "_2_" in a:
        print("its end")
        a = a.replace("_2_","")
        myobj = {'base64': a}
        requests.post(f'http://localhost:5000/postImagePart/{msg.topic}/2',myobj)
        print("request ended")
    print(len(a))


# Create MQTT client
client = mqtt.Client()
client.on_message = on_messageStart 
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_forever()

