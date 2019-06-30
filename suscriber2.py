import paho.mqtt.client as x
def connection(client, user,flag,rc):
    if rc ==0:
        print("connection established")
    c.subscribe("shiv1")
    c.subscribe("shivam123")
def message(client, user, msg):
    topic1 = msg.topic
    data1 = msg.payload.decode()
    print(type(data1))
    return data1
#broker ="192.168.0.116"
def subscriber21():
    c = x.Client("shivam12",False)
    c.connect("broker.hivemq.com",1883)
    c.on_connect = connection
    c.on_message = message
    c.loop_forever()

subscriber21()
