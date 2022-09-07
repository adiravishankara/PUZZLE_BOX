from secrets import *
from Adafruit_IO import Client, Feed
import json

aio_uname, aio_pass = get_aio_cred()

aio = Client("adiravishankara", "aio_LaCq850UiWKjtwPpe0H8tgA5QwGw")
print(aio.feeds())