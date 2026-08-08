I did this display project by the help of Gemini ai and youtube videos.
it require ST7735.py and sysfont.py as extra libraries.

it require :
	-breadboard
	-18 jumper wires
	-one IPS display screen
	-microcontroller (here is using raspberry pi pico)

wiring :
	pin on display -> pin on pico (physical pin) 
	GND -> GND ( 3 or 8 or 13 or 18 or 23 or 28 or 33 or 38)
	VCC -> 3V3 OUT ( 36 )
	SCL -> GP 18 SPI0 SCK ( 24 )
	SDA -> GP 19 SPI0 TX ( 25 )
	RES -> GP 14 (19)
	DC -> GP 15 ( 20 )
	CS -> GP 17 ( 22 )
	BLK -> 3V3 OUT (36) <one or two depending on working or not>

Aung Khant (TUkse)
8.7.2026