import wiringpi
from time import sleep

wiringpi.wiringPiSetup()
wiringpi.pinMode(1, 0)
wiringpi.pinMode(21, 1)

try:
	while True: # endless loop
		if wiringpi.digitalRead(1) == True:
			print("Moving Object Detected")
			sleep(0.5)
			wiringpi.digitalWrite(21, 1)
		else:
			print("No Object Detected")
			sleep(0.5)
			wiringpi.digitalWrite(21, 0)
			
except KeyboardInterrupt:
	wiringpi.pinMode(21, 1)
	wiringpi.digitalWrite(21, 0)
	print("exit")
