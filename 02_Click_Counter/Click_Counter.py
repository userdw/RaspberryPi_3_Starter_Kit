import wiringpi as wpi
from time import sleep

DIGITAL_PUSH_BUTTON = 21

wpi.wiringPiSetup()
wpi.pinMode(DIGITAL_PUSH_BUTTON, wpi.INPUT)

count = 0

try:
	while True:
		if wpi.digitalRead(DIGITAL_PUSH_BUTTON) == wpi.HIGH:
			count = count + 1
			print("Button pressed " + str(count) + " times")
			while wpi.digitalRead(DIGITAL_PUSH_BUTTON) == wpi.HIGH:
				pass
			sleep(0.5)
				
except KeyboardInterrupt:
	print("exit")