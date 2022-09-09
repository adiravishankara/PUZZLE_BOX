import digitalio
import busio
import board
from adafruit_epd.ssd1675 import Adafruit_SSD1675
from adafruit_epd.ssd1680 import Adafruit_SSD1680
from adafruit_epd.epd import Adafruit_EPD
from PIL import Image, ImageDraw, ImageFont


def load_screen():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    ecs = digitalio.DigitalInOut(board.CE0)
    dc = digitalio.DigitalInOut(board.D22)
    rst = digitalio.DigitalInOut(board.D27)
    busy = digitalio.DigitalInOut(board.D17)

    display = Adafruit_SSD1680(  # Newer eInk Bonnet
        # display = Adafruit_SSD1675(   # Older eInk Bonnet
        122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=None, rst_pin=rst, busy_pin=busy)

    display.rotation = 1

    return display

def load_fonts():
    small_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16
    )
    medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    large_font = ImageFont.truetype(
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24
    )
    icon_font = ImageFont.truetype("./meteocons.ttf", 48)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    return small_font, medium_font, large_font, icon_font, WHITE, BLACK

def draw_text(draw, width, height, font, text, fill):
    font_width, font_height = font.getsize(text)
    print(font_width, font_height)
    draw.text((
        width // 2 - font_width // 2,
        height // 2 - font_height // 2
    ), text, font=font, fill=fill)

def run_display(display, value):



def refresh_screen(display):
    display.fill(Adafruit_EPD.WHITE)
    display.display()

def main():
    display = load_screen()
    width = display.width
    height = display.height
    small_font, medium_font, large_font, icon_font, WHITE, BLACK = load_fonts()
    refresh_screen(display)
    image = Image.new("RGB", (width, height), color=BLACK)
    draw = ImageDraw.Draw(image)
    im_1 = draw_text(draw, width, height, small_font, "HELLO", BLACK)

    #display.image(im_1)
    display.display()



if __name__ == '__main__':
    main()