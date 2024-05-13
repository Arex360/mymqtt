import paho.mqtt.client as mqtt
import base64

# MQTT Settings
MQTT_BROKER = "152.67.19.152"  # Change this if your broker is on a different machine
MQTT_PORT = 1883
MQTT_TOPIC = "client9"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received image from topic {msg.topic}")
    
    # Decode base64-encoded image
    image_data = base64.b64decode(msg.payload)
    
    # Save the image to a file
    with open("received_image.jpg", "wb") as f:
        f.write(image_data)
    
    print("Image saved as received_image.jpg")

# Create MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Subscribe to the specified topic
client.subscribe(MQTT_TOPIC)

# Start the loop to listen for messages
client.loop_forever()

