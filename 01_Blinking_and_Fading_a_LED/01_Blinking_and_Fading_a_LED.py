import wiringpi as wpi
from time import sleep

LED_MODULE = 1

wpi.wiringPiSetup() # Must be called before calling any I/O function

def toogleLED(times):
	wpi.pinMode(LED_MODULE, wpi.OUTPUT)
	for i in range(0, times, 1):
		print("on")
		wpi.digitalWrite(LED_MODULE, wpi.HIGH)
		sleep(1)
		print("off")
		wpi.digitalWrite(LED_MODULE, wpi.LOW)
		sleep(1)
		
def fadeLED(times):
	MIN_PWM = 0
	MAX_PWM = 100
	wpi.softPwmCreate(LED_MODULE, MIN_PWM, MAX_PWM) # Set PWM on pin LED_MODULE with initial value = MIN_PWM and range = 100
	
	for i in range(0, times, 1):
		for j in range(MIN_PWM, (MAX_PWM + 1), 1):
			wpi.softPwmWrite(LED_MODULE, j)
			sleep(0.02)
		for j in range(MAX_PWM, (MIN_PWM - 1), -1):
			wpi.softPwmWrite(LED_MODULE, j)
			sleep(0.02)
			
try:
	while True:
		print("Start")
		toogleLED(3)
		sleep(2)
		fadeLED(3)
		sleep(1)
	
except KeyboardInterrupt :
	wpi.pinMode(LED_MODULE, wpi.OUTPUT)
	wpi.digitalWrite(LED_MODULE, wpi.LOW)
	print("exit")