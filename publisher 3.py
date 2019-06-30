import paho.mqtt.client as x
#import mosquito
import time

#broker ="192.168.0.116"
def pub1(msg1):

    c= x.Client("shivam1234",False)
    c.connect("broker.hivemq.com",1883)
#time.sleep(3)
    while True:
        time.sleep(2)
        print("publish data")
        for i in range(0,51):
            time.sleep(1)
            c.publish("shivam123",msg1)
            c.publish("shiv1",i*10)
        #print(ret,ret1)
#c.publish("shivam123","whats going on")
pub1("hello")
