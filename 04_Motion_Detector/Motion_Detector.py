import wiringpi as wpi
from time import sleep

PIR_SENSOR = 1
LED_MODULE = 21

wpi.wiringPiSetup()
wpi.pinMode(PIR_SENSOR, wpi.INPUT)
wpi.pinMode(LED_MODULE, wpi.OUTPUT)

try:
	while True:
		if wpi.digitalRead(PIR_SENSOR) == wpi.HIGH:
			print("Moving Object Detected")
			sleep(0.5)
			wpi.digitalWrite(LED_MODULE, wpi.HIGH)
		else:
			print("No Object Detected")
			sleep(0.5)
			wpi.digitalWrite(LED_MODULE, wpi.LOW)
			
except KeyboardInterrupt:
	wpi.pinMode(LED_MODULE, wpi.OUTPUT)
	wpi.digitalWrite(LED_MODULE, wpi.LOW)
	print("exit")