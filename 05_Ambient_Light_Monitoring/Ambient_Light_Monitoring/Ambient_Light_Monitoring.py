import MCP3202, os
from time import sleep
import wiringpi as wpi

LED_MODULE = 24

wpi.wiringPiSetup()
wpi.softPwmCreate(LED_MODULE, 0, 100)

def translate(value, leftMin, leftMax, rightMin, rightMax):
	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin
	# Convert the left range into a 0 - 1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)
	# Convert the 0 - 1 range into a value in the right range
	return rightMin + (valueScaled * rightSpan)

try:
	while True:
		os.system("clear")
		value1= MCP3202.readADC(1)
		map = translate(value1, 0, 4095, 100, 0)
		print("Ambient Light Monitoring")
		print("Sensor Reading : ", int(value1))
		print("Mapped Value : ", int(map))
		print("")
		print("Press CTRL+C to exit")
		wpi.softPwmWrite(LED_MODULE, int(map))
		sleep(0.02)

except KeyboardInterrupt:
	wpi.pinMode(LED_MODULE, wpi.OUTPUT)
	wpi.digitalWrite(LED_MODULE, wpi.LOW)
	print("exit")
