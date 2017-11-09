import MCP3202
import wiringpi as wpi
import time, os

LED_MODULE = 1
BUZZER_MODULE = 21

wpi.wiringPiSetup()
wpi.pinMode(LED_MODULE, wpi.OUTPUT)
wpi.pinMode(BUZZER_MODULE, wpi.OUTPUT)

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
		value1 = MCP3202.readADC(0) # returns 0 - 4095 representing 0 Volt - VREF Volt
		map = translate(value1, 0, 4095, 255, 0)
		print("Proximity Sensor")
		print("Sensor Reading : ", int(value1))
		print("Mapped Value : ", int(map))
		print("")
		print("Press CTRL+C to exit")
		
		if map <= 200:
			wpi.digitalWrite(LED_MODULE, wpi.HIGH)
			wpi.digitalWrite(BUZZER_MODULE, wpi.HIGH)
			time.sleep(map / 1000)
			wpi.digitalWrite(LED_MODULE, wpi.LOW)
			wpi.digitalWrite(BUZZER_MODULE, wpi.LOW)
			time.sleep(map / 1000)
		else:
			wpi.digitalWrite(LED_MODULE, wpi.HIGH)
			wpi.digitalWrite(BUZZER_MODULE, wpi.HIGH)
			time.sleep(map / 500)
			wpi.digitalWrite(LED_MODULE, wpi.LOW)
			wpi.digitalWrite(BUZZER_MODULE, wpi.LOW)
			time.sleep(map / 500)
		
except KeyboardInterrupt:
	wpi.pinMode(LED_MODULE, wpi.OUTPUT)
	wpi.pinMode(BUZZER_MODULE, wpi.OUTPUT)
	wpi.digitalWrite(LED_MODULE, wpi.LOW)
	wpi.digitalWrite(BUZZER_MODULE, wpi.LOW)
	print("exit")