import wiringpi
from time import sleep

wiringpi.wiringPiSetup()
wiringpi.pinMode(21, 0)
count = 0

try:
	while True: # endless loop
		inputValue = wiringpi.digitalRead(21)
		if inputValue == True:
			count = count + 1
			print("Button pressed " + str(count) + " times")
		sleep(0.3)
		
except KeyboardInterrupt:
	print("exit")
