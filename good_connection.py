import paho.mqtt.client as mqtt # import the client1
import time

def connection(client, userdata, flags, rc):
    if rc == 0:
        print("connection OK")
    else:
        print("Bad connection Returned code =", rc)

broker = "192.168.0.116"
client = mqtt.Client("python1") # create new instance
client.on_connect = connection # bind call back function
print("connecting to broker ",broker)
client.loop_start() # start loop#
client.connect(broker)
client.publish("house/main-light","off")
time.sleep(4)
client.loop_stop() # stop loop
client.disconnect() # disconnect