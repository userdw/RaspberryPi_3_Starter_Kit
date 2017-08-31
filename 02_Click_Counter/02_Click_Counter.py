import wiringpi                 # import library wiringPi-Python
from time import sleep          # import library sleep

wiringpi.wiringPiSetup()        # Must be called before using IO function
wiringpi.pinMode(1,0)           # set pin 1 to 0 (INPUT)
count = 0

while True:                     # endless loop
  # read pin 1, if pin 1 is HUGH (switch presses)
	inputValue = wiringpi.digitalRead(1)            
	if (inputValue == True):
		count = count + 1
		print ("Button pressed " + str(count) + " times")
	sleep(.3)
