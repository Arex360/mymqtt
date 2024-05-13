import paho.mqtt.client as mqtt
import base64
import requests
# MQTT Settings
MQTT_BROKER = "152.67.19.152"  # Change this if your broker is on a different machine
MQTT_PORT = 1883
MQTT_TOPIC = "client9"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received image from topic {msg.topic}")
    url = f'http://localhost:5000/postImage/{msg.topic}'
    myobj = {'base64': msg.payload,'client':msg.topic}
    x = requests.post(url, json = myobj)
    # Decode base64-encoded image
    image_data = base64.b64decode(msg.payload)
    
    # Save the image to a file
    with open("received_image.jpg", "wb") as f:
        f.write(image_data)
    
    print("Image saved as received_image.jpg")

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)
client.loop_forever()

