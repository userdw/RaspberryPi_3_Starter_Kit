import wiringpi
from time import sleep                         # import library WiringPi-Python

wiringpi.wiringPiSetup()                       # Must be called before using IO function
wiringpi.pinMode(3,0)                          # Set pin 0 to 0 (INPUT)
wiringpi.pinMode(4,1)                          # Set pin 1 to 1 (OUTPUT)

while True:                                    # endless loop
        if wiringpi.digitalRead(3)== 1:        # read pin 0, if pin 1 is 0 (LOW)
                print "Moving Object Detected"
		#sleep(0.5)
		wiringpi.digitalWrite(4,1)     # if True, write pin 0 to 1 (HIGH)
        else:
                print "No Object Detected"
		#sleep(0.5)
		wiringpi.digitalWrite(4,0)     # if False, write pin 0 to 0 (LOW)



