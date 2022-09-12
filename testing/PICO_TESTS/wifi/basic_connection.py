import network
import secrets
import time

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.SSID, secrets.PASSWORD)

    while not wlan.isconnected:
        print('Waiting for a Connection')
        time.sleep(0.5)
    print('Connected!')
    print(wlan.ifconfig())


if __name__ == '__main__':
    connect()
