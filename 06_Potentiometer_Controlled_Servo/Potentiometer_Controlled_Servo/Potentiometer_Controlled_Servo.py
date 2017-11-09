import MCP3202, os
from time import sleep
import wiringpi as wpi

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
		map = translate(value1, 0, 4095, 6, 24)
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
