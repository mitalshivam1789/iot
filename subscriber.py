import paho.mqtt.client as x
def connection(client, user,flag,rc):
	if rc ==0:
		print("connection established")
	c.subscribe("shivam123",False,transport="websockets")

def message(client, user, msg):
	print(msg.payload.decode())
	data1 = msg.payload.decode()
	print(data1)
	print(type(data1))
	if data1 == "40":
		print("turn on led")
broker ="192.168.0.116"
c= x.Client("shivam12")
c.connect("broker.hivemq.com",1883)
c.on_connect = connection
c.on_message=message
c.loop_forever()