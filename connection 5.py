# if we put wrong ip address then the given programme will show an error msg insted of giving an error
# using try and except method of the python
# in this we are also handling the authentication error on the client side only
# using the flag "client.bad_connection_flag = True"
import paho.mqtt.client as mqtt # import the client1
import time
import sys

def on_disconect(client,userdata, flag,rc =0):
    print("DisConnected flags" + "result code" + str(rc))
    client.connected_flag = False
def connection(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True #set flag
        print("connection OK")
    else:
        print("Bad connection Returned code =", rc)
        #client.loop_stop()
        client.bad_connection_flag = True  #
mqtt.Client.connected_flag = False #create flag in class
mqtt.Client.bad_connection_flag = False#
broker = "192.168.0.116"
client = mqtt.Client("python1") # create new instance
client.on_connect = connection # bind call back function
print("connecting to broker ",broker)
try:
    client.connect(broker) # connect to broker
except:
    print("can't connect")
    sys.exit(1)
client.loop_start() # start loop#
while not client.connected_flag and not client.bad_connection_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
    if client.bad_connection_flag:
        client.loop_stop()
        sys.exit()
print("in main loop")
client.publish("house/main-light","off")
time.sleep(4)
client.loop_stop() # stop loop
client.disconnect() # disconnect