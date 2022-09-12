from machine import Pin, Timer
from time import sleep

class Motor:
    def __init__(self, pin1, pin2):
        self.pin1 = Pin(pin1, Pin.OUT)
        self.pin2 = Pin(pin2, Pin.OUT)

        self.pin1.value(0)
        self.pin2.value(0)

    def forward(self):
        self.pin1.value(1)
        sleep(2)
        self.pin1.value(0)

    def backward(self):
        self.pin2.value(0)
        sleep(2)
        self.pin2.value(0)


if __name__ == "__main__":
    A = Motor(24, 25)
    A.forward()
    A.backward()
