import MCP3202
import wiringpi,time,os
from time import strftime
wiringpi.wiringPiSetup()
wiringpi.pinMode(1,1)
wiringpi.pinMode(21,1)

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
		os.system('clear')
		value1= MCP3202.readADC(0)	# range data 0 - vref (volt)
		map=translate(value1,0,4096,255,0)
		print "Proximity Sensor"
		print "Curent Distance : ",int(value1),int(map)
		print ""
		print "Press CTRL+C to exit"
		if map <= 200:
			wiringpi.digitalWrite(1,1)
			wiringpi.digitalWrite(21,1)
			time.sleep(map/1000)
			# Write 0 (Low) / 1 (High) to Buzzer and LED
			wiringpi.digitalWrite(1,0)
			wiringpi.digitalWrite(21,0)
			time.sleep(map/1000)
		else:
			# Write 1 (High) / 0 (Low) to Buzzer and Led
			wiringpi.digitalWrite(1,1)
			wiringpi.digitalWrite(21,1)
			time.sleep(map/500)
			# Write 0 (Low) / 1 (High) to Buzzer and LED
			wiringpi.digitalWrite(1,0)
			wiringpi.digitalWrite(21,0)
			time.sleep(map/500)
		
except KeyboardInterrupt:
	wiringpi.digitalWrite(1,0)
	wiringpi.digitalWrite(21,0)
	print "exit"
