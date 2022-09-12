import network
import secrets
import time
import urequests as requests


class AIO_handler:
    def __init__(self):
        self.WLAN_SSID = secrets.WLAN_SSID
        self.WLAN_PWD = secrets.WLAN_PASSWORD
        self.AIO_UNAME = secrets.AIO_UNAME
        self.AIO_KEY = secrets.AIO_KEY
        self.connect_to_wifi()

    def connect_to_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.WLAN_SSID, self.WLAN_PWD)

        while not wlan.isconnected:
            print('Waiting for a Connection')
            time.sleep(0.5)
        print('Connected!')
        #print(wlan.ifconfig())

    def update_AIO(self, feed, value):
        url = 'https://io.adafruit.com/api/v2/{}/feeds/{}/data'.format(self.AIO_UNAME, feed)
        body = {'value': value}
        headers = {'X-AIO-Key': self.AIO_KEY, 'Content-Type': 'application/json'}

        try:
            update = requests.post(url, json=body, headers=headers)
            print(update.text)
        except Exception as f:
            print(f)

    def update_temperature_feed(self, value):
        try:
            self.update_AIO('current-data.temperature', value)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    A = AIO_handler()
    for i in range(10):
        A.update_temperature_feed(i)
        time.sleep(10)
