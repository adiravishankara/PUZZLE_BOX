from secrets import *
import requests

tzdb_key = get_tzdb_cred()
owm_key = get_owm_cred()

def get_time(timezone="Asia/Tokyo"):
    result = requests.get("http://api.timezonedb.com/v2.1/get-time-zone?key="
        "{}&format=json&by=zone&zone={}".format(tzdb_key, timezone)).json()
    date, time = result["formatted"].split(" ")
    return date, time


def get_weather(location="Nakano"):
    lat = "35.707808"
    lon = "139.669662"
    api_key = "1376990aa10ca1cb3f9f6d0000eb8efc"
    result = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric".format(lat, lon, owm_key)).json()
    weather = result

    print(weather)


if __name__ == '__main__':
    get_weather()
    print(get_time())