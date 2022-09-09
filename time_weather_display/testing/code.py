import time
from secrets import get_owm_cred, get_tzdb_cred
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
        #schedule.every(15).seconds.do(lambda: self.update_screen())
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)

    def update_time(self):
        self.graphics.parse_time(get_time())

    def update_weather(self):
        self.graphics.parse_weather_info(get_weather())

    def update_screen(self):
        self.update_time()
        self.update_weather()
        self.graphics.draw_display()
        self.display.update_screen_full(self.graphics.image)

    def set_screen(self, text, color, font, image=None):
        self.cur_image = self.graphics.draw_text("HELLO", self.graphics.BLACK, self.graphics.small_font)
        self.display.update_screen_partial()



if __name__ == '__main__':
    A = time_weather_display()
    A.set_screen()


