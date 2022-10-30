from api_calls import *
from aio_interface import *
import schedule


class currentDataUpdater:
    def __init__(self):
        self.AIO = AIO_INTERFACE()
        #self.AIO.list_feeds()
        self.time_feed = self.AIO.add_new_feed('current-data.time')
        self.temp_feed = self.AIO.add_new_feed('current-data.temperature')
        self.weather_feed = self.AIO.add_new_feed('current-data.weather')

    def update_time(self):
        print(get_time()[1])
        self.AIO.update_feed(self.time_feed, get_time()[1])

    def update_temp(self):
        self.AIO.update_feed(self.temp_feed, get)


if __name__ == '__main__':
    A = currentDataUpdater()
    A.update_time()
