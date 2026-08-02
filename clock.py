import time
from datetime import datetime

while True:
	now = datetime.now()

	print(now.strftime("%H:%M:%S"), end ="\r")
	time.sleep(1)
