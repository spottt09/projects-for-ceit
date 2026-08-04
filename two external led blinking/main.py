from machine import Pin
from time import sleep

led0 = Pin(2, Pin.OUT)
led1 = Pin(13, Pin.OUT)


while True:
    led0.on()
    sleep(0.5)
    led1.on()
    sleep(0.25)

    led0.off()
    sleep(0.5)
    led1.off()
    sleep(0.25)
