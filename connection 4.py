

import paho.mqtt.client as mqtt # import the client1
import time
import sys
def connection(client, userdata, flags, rc):

    if rc == 0:
        client.connected_flag = True #set flag
        print("connection OK")
    else:
        print("Bad connection Returned code =", rc)
        client.loop_stop()
mqtt.Client.connected_flag = False #create flag in class
broker = "192.168.0.116"
client = mqtt.Client("python1") # create new instance
client.on_connect = connection # bind call back function
print("connecting to broker ",broker)
# this part is used to check if ip address is correct.
# and not correct then it will go to the except and excit the sys fun
#
try:
    client.connect(broker) # connect to broker
except:
    print("can't connect")
    sys.exit(1)

#------------------------
client.loop_start() # start loop#
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in main loop")
client.publish("house/main-light","off")
time.sleep(4)
client.loop_stop() # stop loop
client.disconnect() # disconnect