import wiringpi                 # import library wiringPi-Python
from time import sleep          # import library sleep

wiringpi.wiringPiSetup()        # Must be called before using IO function
wiringpi.pinMode(21,0)           # set pin 2 to 0 (INPUT)
count = 0
try:
while True:                     # endless loop
  # read pin 1, if pin 1 is HUGH (switch presses)
	inputValue = wiringpi.digitalRead(21)            
	if (inputValue == True):
		count = count + 1
		print ("Button pressed " + str(count) + " times")
	sleep(.3)
except KeyboardInterrupt:
	print "exit"
