from Adafruit_IO import Client,Feed
import random as r
import time

aio = Client("mittalshivam12","d4d2aee4c7624716ab2cc6559789d687")
#feed = Feed(name='try_once')
#response = aio.create_feed(feed)
while True:
    time.sleep(1)
    data = r.randint(1,10)
    test = aio.send_data('counter',data)