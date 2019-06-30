# a publishing programme
import paho.mqtt.client as mqtt # import the client1
import time

def on_log(client,userdata,level, buf):
    print(buf)
def connection(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True #set flag
        print("connection OK")
    else:
        print("Bad connection Returned code =", rc)
        client.loop_stop()
def on_disconnect(client,userdata,rc):
    print("client disconnected ok")
def on_publish(client, userdata, mid):
    print("In on_pub callback mid = "+str(mid))
def on_subscribe(client, userdata,mid,granted_qos):
    print("subscribed")
def on_message(client,userdate,message):
    topic = message.topic
    msgr = str(message.payload.decode("utf-8"))
    msgr = "Message Received" + msgr
    print(msgr)
def reset():
    ret = client.publish("house/light","",0,True)


broker = "192.168.0.116"
port = 1883
mqtt.Client.connected_flag = False #create flag in class
client = mqtt.Client("python1") # create new instance
client.on_log = on_log
client.on_connect = connection # bind call back function
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(broker,port) #connect to broker
print("connecting to broker ",broker)
#client.connect(broker) # connect to broker
client.loop_start() # start loop#
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in main loop")
ret = client.publish("house/light","off",0,True)
print("published return ",ret)
time.sleep(4)
client.subscribe("house/light",0)
time.sleep(10)
client.loop_stop() # stop loop
client.disconnect() # disconnect