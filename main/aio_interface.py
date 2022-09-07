from secrets import *
from Adafruit_IO import Client, Feed
import json

aio_uname, aio_pass = get_aio_cred()

aio = Client("adiravishankara", "aio_qdSC53dZVejYLxotWcONTIrqXtAL")
print(aio.feeds())

pico_feed = aio.feeds('pico')

aio.send_data(pico_feed.key, str(100))