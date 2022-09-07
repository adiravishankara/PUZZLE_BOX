from secrets import *
from Adafruit_IO import Client, Feed
import json


class AIO_INTERFACE:
    def __init__(self):
        self.aio_uname, self.aio_pass = get_aio_cred()
        self.aio = Client(self.aio_uname, self.aio_pass)

    def add_new_feed(self, feed_name):
        return self.aio.feeds(feed_name)

    def update_feed(self, feed, value):
        self.aio.send_data(feed.key, value)

    def list_feeds(self):
        print(self.aio.feeds())

