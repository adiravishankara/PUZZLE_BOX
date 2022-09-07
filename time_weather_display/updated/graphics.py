from PIL import Image, ImageDraw, ImageFont


class graphics:
    def __init__(self, display):
        self.d_width = display.width
        self.d_height = display.height

        self.load_fonts()
        self.load_icon_map()

    def load_fonts(self):
        self.small_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16
        )
        self.medium_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
        self.large_font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24
        )
        self.icon_font = ImageFont.truetype("./meteocons.ttf", 48)

    def load_icon_map(self):
        self.ICON_MAP = {
            "01d": "B",
            "01n": "C",
            "02d": "H",
            "02n": "I",
            "03d": "N",
            "03n": "N",
            "04d": "Y",
            "04n": "Y",
            "09d": "Q",
            "09n": "Q",
            "10d": "R",
            "10n": "R",
            "11d": "Z",
            "11n": "Z",
            "13d": "W",
            "13n": "W",
            "50d": "J",
            "50n": "K"}
        # RGB Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def parse_weather_info(self, weather, celsius=True, feels_like=False, description=True):
        if feels_like:
            self.temperature = weather["main"]["feels_like"]
        else:
            self.temperature = weather["main"]["temp"]
            print(self.temperature)

        if not celsius:
            self.temperature = "{} °F".format((self.temperature * 9 / 5 ) + 32)
        else:
            self.temperature = "{} °C".format(self.temperature)

        self.weather_condition = weather["weather"][0]["main"]

        if description:
            self.weather_description = weather["weather"][0]["description"]
            self.weather_description = "{} {}".format(self.weather_condition[0].upper(), self.weather_condition[1:])
        else:
            self.weather_description = None

        self.city_name = "{}, {}".format(weather["name"], weather["sys"]["country"])

        self._weather_icon = self.ICON_MAP[weather["weather"][0]["icon"]]

    def parse_time(self, time_data, date=True):
        if date:
            self.date = time_data[0]
        else:
            self.date = None

        self.current_time = time_data[1]

    def draw_display(self, WHITEBG=True):
        if WHITEBG:
            self.image = Image.new("RGB", (self.d_width, self.d_height), color=self.WHITE)
            self.fill_color = self.BLACK
        else:
            self.image = Image.new("RGB", (self.d_width, self.d_height), color=self.BLACK)
            self.fill_color = self.WHITE
        self.draw = ImageDraw.Draw(self.image)

        self.draw_weather_icon()
        self.draw_temperature()
        self.draw_weather_condition()
        self.draw_weather_description()
        self.draw_city_name()
        self.draw_time()


    def draw_weather_icon(self):
        self.font_width, self.font_height = self.icon_font.getsize(self._weather_icon)
        self.draw.text(
            (
                self.d_width // 2 - self.font_width // 2,
                self.d_height // 2 - self.font_height // 2 - 5,
            ),

            self._weather_icon, font=self.icon_font, fill=self.fill_color)

    def draw_temperature(self):
        self.font_width, self.font_height = self.large_font.getsize(self.temperature)
        self.draw.text((
                self.d_width - self.font_width - 5,
                self.d_height - self.font_height * 2,
            ),self.temperature, font=self.large_font, fill=self.fill_color)

    def draw_city_name(self):
        self.draw.text((5, 5), self.city_name, font=self.medium_font, fill=self.fill_color)

    def draw_weather_condition(self):
        self.font_width, self.font_height = self.large_font.getsize(self.weather_condition)
        self.draw.text((
            5,
            self.d_height - self.font_height * 2,
        ), self.weather_condition, font=self.large_font, fill=self.fill_color)

    def draw_weather_description(self):
        self.font_width, self.font_height = self.small_font.getsize(self.weather_description)
        self.draw.text((
            5,
            self.d_height - self.font_height - 5,
        ), self.weather_description, font=self.small_font, fill=self.fill_color)

    def draw_time(self):
        self.font_width, self.font_height = self.medium_font.getsize(self.current_time)
        self.draw.text((
            5,
            self.font_height * 2 - 5,
        ), self.current_time, font=self.medium_font, fill=self.fill_color)






