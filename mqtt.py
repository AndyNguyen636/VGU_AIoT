import sys
from Adafruit_IO import MQTTClient
import random
import time
AIO_USERNAME = "NguyenDuyTruong"
AIO_KEY = "aio_TLTH59WBtszmqx8Ijwnjes2KzmmY"

def connected(client):
    print("Server connected ...")
    client.subscribe("button1")
    client.subscribe("button2")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe!!!")

def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected  #function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()

while True:
    time.sleep(5)
    client.publish("sensor1", random.randint(10,50))
    client.publish("sensor2", random.randint(0,100))
    client.publish("sensor3", random.randint(12,24))
    pass
