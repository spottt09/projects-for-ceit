from machine import Pin, SPI
import ST7735
import time
import sysfont


spi = SPI(0, baudrate=20000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(19))


display = ST7735.TFT(spi, 15, 14, 17)
display.initr()
display.rotation(1)
display.fill(ST7735.TFTColor(255, 0, 0))


display.fill(0)
display.text((40, 60), "LOVE U", ST7735.TFTColor(255, 255, 255), sysfont.sysfont,3)
