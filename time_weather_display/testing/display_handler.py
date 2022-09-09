import digitalio
import busio
import board
from adafruit_epd.ssd1675 import Adafruit_SSD1675
from adafruit_epd.ssd1680 import Adafruit_SSD1680
from adafruit_epd.epd import Adafruit_EPD


class display_hander:
    def __init__(self):
        self.load_screen()
        # self.load_fonts()
        # self.load_icon_map()

    def load_screen(self):
        spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
        ecs = digitalio.DigitalInOut(board.CE0)
        dc = digitalio.DigitalInOut(board.D22)
        rst = digitalio.DigitalInOut(board.D27)
        busy = digitalio.DigitalInOut(board.D17)

        self.display = Adafruit_SSD1680(  # Newer eInk Bonnet
            # display = Adafruit_SSD1675(   # Older eInk Bonnet
            122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=None, rst_pin=rst, busy_pin=busy)

        self.display.rotation = 1

    def update_screen_full(self, image):
        self.display.fill(Adafruit_EPD.WHITE)
        self.display.image(image)
        self.display.display()

    def update_screen_partial(self, image):
        self.display.image(image)
        self.display.display()

    def refresh_screen(self):
        self.display.fill(Adafruit_EPD.WHITE)
        self.display.display()


if __name__ == '__main__':
    display = display_hander()
    image = Image.new("RGB", (display.display.width, display.display.height), color=display.WHITE)
    draw = ImageDraw.Draw(image)
    icon = display.ICON_MAP["09d"]
    (font_width, font_height) = display.icon_font.getsize(icon)
    draw.text(
        (
            display.display.width // 2 - font_width // 2,
            display.display.height // 2 - font_height // 2 - 5,
        ),
        icon,
        font=display.icon_font,
        fill=display.BLACK)
    display.update_screen_full(image)





