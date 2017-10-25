import wiringpi	                	# import library WiringPi-Python
from time import sleep          	# import library sleep

wiringpi.wiringPiSetup()        	# Must be called before using IO function
wiringpi.pinMode(1,1)           	# Set pin 9 to 1 (OUTPUT) / 0 (INPUT)
wiringpi.softPwmCreate(1,0,100)		# Set PWM on pin 9, start value 0, max value 100
LED_MODULE = 1

def toogleLED(times):
	for i in range (0,times,1):
		print "on"
		wiringpi.digitalWrite(LED_MODULE, not wiringpi.digitalRead(LED_MODULE))
		sleep(1)
		print "off"
		wiringpi.digitalWrite(LED_MODULE, not wiringpi.digitalRead(LED_MODULE))
		sleep(1) 
		
def fadeLED(times):
	for i in range (0,times,1):
		for j in range (0,100,1):
			wiringpi.softPwmWrite(LED_MODULE,j)	# PWM pulse on pin 9
			sleep(0.02)
		for j in range (100,0,-1):
			wiringpi.softPwmWrite(LED_MODULE,j)	# PWM pulse on pin 9
			sleep(0.02)
		wiringpi.softPwmWrite(LED_MODULE,0)
		
try:
 while  True :
	print "Start"
	toogleLED(3)
	sleep(2)
	fadeLED(3)
	sleep(1)

except KeyboardInterrupt :
	wiringpi.digitalWrite(LED_MODULE,0)
	wiringpi.softPwmWrite(LED_MODULE,0)			# PWM pulse on pin 0
	print "exit"
