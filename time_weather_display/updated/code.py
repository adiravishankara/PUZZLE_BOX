import time
import urllib.request
import urllib.parse
import digitalio
import busio
import board
from adafruit_epd.ssd1675 import Adafruit_SSD1675
from adafruit_epd.ssd1680 import Adafruit_SSD1680
from secrets import *
import schedule
from graphics import *
from display_handler import *
from api_calls import *


class time_weather_display:
    def __init__(self):
        self.display = display_hander()
        self.graphics = graphics(self.display.display)
        self.tzdb_key = get_tzdb_cred()
        self.owm_key = get_owm_cred()
        self.update_screen()
        schedule.every(1).minute.do(self.update_screen())
        while True:
            schedule.run_pending()
            time.sleep(1)

    def update_time(self):
        self.graphics.parse_time(get_time())

    def update_weather(self):
        self.graphics.parse_weather_info(get_weather())

    def update_screen(self):
        self.update_time()
        self.update_weather()
        self.graphics.draw_display()
        self.display.update_screen_full(self.graphics.image)


if __name__ == '__main__':
    time_weather_display()


