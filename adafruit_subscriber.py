from Adafruit_IO import MQTTClient
import time
feedid = "counter"
def connect(client):
    client.subscribe(feedid)

def message(c,u,payload):
    print(payload)

client = MQTTClient("mittalshivam12","d4d2aee4c7624716ab2cc6559789d687")
client.on_connect = connect
client.on_message = message
#time.sleep(1)
client.connect()
client.loop_blocking()