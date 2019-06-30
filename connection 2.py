# program in which we wait in the for loop for the connection establishment

import paho.mqtt.client as mqtt # import the client1
import time

def connection(client, userdata, flags, rc):
    rc=2 # when rc is different then it will wait for the rc=0
    # but here we put it manually tocheck
    if rc == 0:
        client.connected_flag = True #set flag
        print("connection OK")
    else:
        print("Bad connection Returned code =", rc)

mqtt.Client.connected_flag = False #create flag in class
broker = "192.168.0.116"
client = mqtt.Client("python1") # create new instance
client.on_connect = connection # bind call back function
print("connecting to broker ",broker)
client.connect(broker) # connect to broker
client.loop_start() # start loop#
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in main loop")
client.publish("house/main-light","off")
time.sleep(4)
client.loop_stop() # stop loop
client.disconnect() # disconnect