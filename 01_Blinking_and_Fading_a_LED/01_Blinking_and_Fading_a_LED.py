
import wiringpi	                # import library WiringPi-Python
from time import sleep          # import library sleep

wiringpi.wiringPiSetup()        # Must be called before using IO function
wiringpi.pinMode(4,1)           # Set pin 0 to 1 (OUTPUT) / 0 (INPUT)
wiringpi.softPwmCreate(4,0,100)		# Set PWM on pin 0, start value 0, max value 100
LED_MODULE = 4

def toogleLED(times):
	for i in range (0,times,1):
		wiringpi.digitalWrite(LED_MODULE, not wiringpi.digitalRead(LED_MODULE))
		sleep(0.25) 
		wiringpi.digitalWrite(LED_MODULE,not wiringpi.digitalRead(LED_MODULE))
		sleep(0.25)

def fadeLED(times):
	for i in range (0,times,1):
		for j in range (0,100,1):
			wiringpi.softPwmWrite(LED_MODULE,j)		# PWM pulse on pin 0
			sleep(0.01)
		for j in range (100,0,-1):
			wiringpi.softPwmWrite(LED_MODULE,j)		# PWM pulse on pin 0
			sleep(0.01)

try:
 while  True :
	toogleLED(3)
	print "blink led finish"
	sleep(1)
	fadeLED(3)
	print "fade led finish"
	sleep(1)
except KeyboardInterrupt :
	wiringpi.softPwmWrite(LED_MODULE,0)		# PWM pulse on pin 0
	print "exit"


	

