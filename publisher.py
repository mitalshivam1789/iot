import paho.mqtt.client as x
#import mosquito
import time
#broker ="192.168.0.116"
c= x.Client("shivam1234",False,transport = "websockets")
c.connect("broker.hivemq.com",8000,keepalive= 3)
#time.sleep(3)
while True:
    time.sleep(2)
    print("publish data")
    for i in range(0,51):
        time.sleep(1)
        c.publish("shivam123",i,qos=2)
#c.publish("shivam123","whats going on")

