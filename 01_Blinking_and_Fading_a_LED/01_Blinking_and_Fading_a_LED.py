import wiringpi # import library WiringPi-Python
from time import sleep # import library sleep

LED_MODULE = 1
wiringpi.wiringPiSetup() # Must be called before using IO function

def toogleLED(times):
	wiringpi.pinMode(LED_MODULE, 1) # Set pin 9 to 1 (OUTPUT) / 0 (INPUT)
	for i in range(0, times, 1):
		print("on")
		wiringpi.digitalWrite(LED_MODULE, 1)
		sleep(1)
		print("off")
		wiringpi.digitalWrite(LED_MODULE, 0)
		sleep(1)
		
def fadeLED(times):
	MIN_PWM = 0
	MAX_PWM = 100
	wiringpi.softPwmCreate(LED_MODULE, MIN_PWM, MAX_PWM) # Set PWM on pin 9, start value 0, max value 100
	
	for i in range(0, times, 1):
		for j in range(MIN_PWM, (MAX_PWM + 1), 1):
			wiringpi.softPwmWrite(LED_MODULE, j) # PWM pulse on pin 9
			sleep(0.02)
		for j in range(MAX_PWM, (MIN_PWM - 1), -1):
			wiringpi.softPwmWrite(LED_MODULE, j) # PWM pulse on pin 9
			sleep(0.02)
			
try:
	while True :
		print("Start")
		toogleLED(3)
		sleep(2)
		fadeLED(3)
		sleep(1)
	
except KeyboardInterrupt :
	wiringpi.pinMode(LED_MODULE, 1) # Set pin 9 to 1 (OUTPUT) / 0 (INPUT)
	wiringpi.digitalWrite(LED_MODULE, 0)
	print("exit")
