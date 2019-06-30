#import paho.mqtt.client as x
from Adafruit_IO import MQTTClient
import time
import random
#import mosquito
import time
#broker = "io.adafruit.com"
#port = 1883
username = "mittalshivam12"
password="d4d2aee4c7624716ab2cc6559789d687"
#broker ="192.168.0.116"
c= MQTTClient(username,password)

c.connect()

#c.connect("broker.hivemq.com",1883)
#time.sleep(3)
while True:
    time.sleep(1)
    value = random.randint(0,100)
    print("publishing {0} to DemoFeed.".format(value))
    c.publish("data",value)