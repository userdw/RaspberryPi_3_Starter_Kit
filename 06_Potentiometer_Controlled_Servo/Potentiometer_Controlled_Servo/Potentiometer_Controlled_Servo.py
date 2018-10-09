import MCP3202, os
from time import sleep
import wiringpi as wpi

#		       90(15)
#			 ^
#		 	 |
#		 	 |
#			 |
#            0(6) <------*-----> 180 (24)
# Each “cycle” of PWM output takes 10mS with the default range value of 100,
# so trying to change the PWM value more than 100 times a second will be futile.

MICRO_SERVO = 1

wpi.wiringPiSetup()
wpi.softPwmCreate(MICRO_SERVO, 0, 200)

def translate(value,leftMin,leftMax,rightMin,rightMax):
	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin
	# Convert the left range into a 0-1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)
	# Convert the 0-1 range into a value in the right range.
	return rightMin + (valueScaled * rightSpan)

try:
	while True:
		os.system("clear")
		value1 = MCP3202.readADC(0)
		map = translate(value1, 0, 4095, 6, 24)		# Range from 0.6 milisecond until 2.4 milisecond
		position = translate (value1, 0, 4095, 0, 180)
		print("Servo Position")
		print("Curent Position : ", int(position), "degree")
		print("")
		print("Press CTRL+C to exit")
		wpi.softPwmWrite(MICRO_SERVO, int(map))
		sleep(0.001)

except KeyboardInterrupt:
	wpi.pinMode(MICRO_SERVO, wpi.OUTPUT)
	wpi.digitalWrite(MICRO_SERVO, wpi.LOW)
	print("exit")
