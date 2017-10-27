import MCP3202, wiringpi, time, os
from time import sleep

wiringpi.wiringPiSetup()
wiringpi.softPwmCreate(24, 0, 100)

def translate(value, leftMin, leftMax, rightMin, rightMax):
	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin
	# Convert the left range into a 0 - 1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)
	# Convert the 0 - 1 range into a value in the right range
	return rightMin + (valueScaled * rightSpan)

try:
	while True: # endless loop
		os.system("clear")
		value1= MCP3202.readADC(1)
		map = translate(value1, 0, 4095, 100, 0)
		print("Ambient Light Monitoring")
		print("Curent Light : ", int(map), "%")
		print("")
		print("Press CTRL+C to exit")
		wiringpi.softPwmWrite(24, int(map)) # PWM pulse on pin 24
		sleep(0.02) # delay for 20ms
		wiringpi.softPwmWrite(24, int(map)) # PWM pulse on pin 24
		sleep(0.02) # delay for 20ms

except KeyboardInterrupt:
	wiringpi.pinMode(24, 1)
	wiringpi.digitalWrite(24, 0)
	print("exit")
