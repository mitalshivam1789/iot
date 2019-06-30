# if we put wrong ip address then the given programme will show an error msg insted of giving an error
# using try and except method of the python
# in this we are also handling the authentication error on the client side only
# using the flag "client.bad_connection_flag = True"
# authentication error is the ack error that come and we check it using "rc"
import paho.mqtt.client as mqtt # import the client1
import time
import sys

def on_log(client,userdata,level, buf):
    print("log: ",buf)
def on_disconect(client,userdata, flag,rc =0):
    print("DisConnected flags" + "result code" + str(rc) + "client_id ")
    client.connected_flag = False
def connection(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True #set flag
        print("connection OK")
    else:
        print("Bad connection Returned code =", rc)
        #client.loop_stop()
        #client.bad_connection_flag = True  # making flag for the checking the authentication error


mqtt.Client.connected_flag = False #create flag in class
#mqtt.Client.bad_connection_flag = False
broker = "192.168.0.116"
client = mqtt.Client("python1") # create new instance
client.on_log =on_log #client logging
client.on_connect = connection # bind call back function
client.on_disconnect = on_disconect # bind call back function
print("connecting to broker ",broker)
client.loop_start()
try:
    client.connect(broker) # connect to broker
    while not client.connected_flag:  # wait in loop
        print("In wait loop")
        time.sleep(1)
except:
    print("can't connect")
    sys.exit("quitting")

run_flag = True
count = 1
while run_flag:
    print("in main loop")
    msg ="test message" + str(count)
    ret = client.publish("house/2",msg,0)
    print("publish",ret)
    count +=1
    time.sleep(4)
client.loop_stop() # stop loop
client.disconnect() # disconnect