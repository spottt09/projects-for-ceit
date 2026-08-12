from machine import Pin, SPI
from time import sleep
import ST7735
import sysfont
spi = SPI(0, baudrate=8000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))
button = Pin(13, Pin.IN, Pin.PULL_UP)
display = ST7735.TFT(spi, 15, 14, 17)
display.initr()
display.rotation(1)
last_state = -1
while True:
    current_state = button.value()
    if current_state != last_state:
        if current_state == 0:
            display.fill(ST7735.TFTColor(255, 50, 500))
            display.text((40,60), "pressed", ST7735.TFTColor(255, 255, 255), sysfont.sysfont,3)
        else:
            display.fill(ST7735.TFTColor(255, 700, 600))
            display.text((40,60), "press", ST7735.TFTColor(300, 777, 700), sysfont.sysfont,3)
        last_state = current_state   
    sleep(0.05)
