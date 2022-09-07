from secrets import *
from Adafruit_IO import Client, Feed
import json

aio_uname, aio_pass = get_aio_cred()

aio = Client("adiravishankara", "aio_VQmJ25zRMeTED2cw3xSZegTKxfdx")
print(aio.feeds())

pico_feed = aio.feeds('pico')

aio.send_data(pico_feed.key, str(100))