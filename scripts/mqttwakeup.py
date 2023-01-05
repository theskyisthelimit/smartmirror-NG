import paho.mqtt.client as mqtt
import subprocess
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing to the topic "/home/this/that/on"
    client.subscribe("homeassistant/binary_sensor/eingang_sensor_motion/state")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.payload.decode() == "on":
        subprocess.call("sh monitor_on.sh", shell=True)
    elif msg.payload.decode() == "off":
        subprocess.call("sh monitor_off.sh", shell=True)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.4", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()