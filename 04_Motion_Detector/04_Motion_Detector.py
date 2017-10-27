import wiringpi
from time import sleep

wiringpi.wiringPiSetup() # Must be called before using IO function
wiringpi.pinMode(1, 0) # Set pin 1 to 0 (INPUT)
wiringpi.pinMode(21, 1) # Set pin 21 to 1 (OUTPUT)

try:
	while True: # endless loop
		if wiringpi.digitalRead(1) == True:
			print("Moving Object Detected")
			sleep(0.5)
			wiringpi.digitalWrite(21, 1) # if True, write pin 21 to 1 (HIGH)
		else:
			print("No Object Detected")
			sleep(0.5)
			wiringpi.digitalWrite(21, 0) # if False, write pin 21 to 0 (LOW)
			
except KeyboardInterrupt:
	wiringpi.pinMode(21, 1)
	wiringpi.digitalWrite(21, 0)
	print("exit")
