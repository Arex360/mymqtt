import paho.mqtt.publish as publish
import base64

# MQTT Settings
MQTT_BROKER = "152.67.19.152"
MQTT_PORT = 1883
MQTT_TOPIC = "client9"

# Read the image file
def read_image_file(file_path):
    with open(file_path, "rb") as f:
        image_data = f.read()
    return image_data

# Encode the image data to base64
def encode_image_to_base64(image_data):
    return base64.b64encode(image_data)

# Publish the image to the MQTT broker
def publish_image(image_path):
    image_data = read_image_file(image_path)
    encoded_image = encode_image_to_base64(image_data)
    publish.single(MQTT_TOPIC, encoded_image, hostname=MQTT_BROKER, port=MQTT_PORT)

if __name__ == "__main__":
    # Path to the image file
    image_path = "01.png"
    
    # Publish the image to the MQTT broker
    publish_image(image_path)
