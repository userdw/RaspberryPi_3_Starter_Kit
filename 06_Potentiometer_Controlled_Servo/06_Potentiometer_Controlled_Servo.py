import MCP3202, wiringpi, os
from time import sleep

wiringpi.wiringPiSetup()
wiringpi.softPwmCreate(1, 0, 200)

def translate(value,leftMin,leftMax,rightMin,rightMax):
	# Figure out how 'wide' each range is
    	leftSpan = leftMax - leftMin
    	rightSpan = rightMax - rightMin
    	# Convert the left range into a 0-1 range (float)
    	valueScaled = float(value - leftMin) / float(leftSpan)
    	# Convert the 0-1 range into a value in the right range.
    	return rightMin + (valueScaled * rightSpan)

try:
	while 1: # endless loop
		os.system("clear")
		value1 = MCP3202.readADC(0)
		map = translate(value1, 0, 4095, 6, 24)
		position = translate (value1, 0, 4095, 0, 180)
 		print("Servo Position")
		print("Curent Position : ", int(position), "degree")
    		print("")
		print("Press CTRL+C to exit")
		wiringpi.softPwmWrite(1, int(map))
		sleep(0.001)

except KeyboardInterrupt:
	wiringpi.pinMode(1, 1)
	wiringpi.digitalWrite(1, 0)
	print("exit")

