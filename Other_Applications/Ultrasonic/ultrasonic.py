import wiringpi as wpi
import time                                	#Import time library

wpi.wiringPiSetup() # Must be called before calling any I/O function

TRIG = 25                                 	#Associate pin 23 to TRIG
ECHO = 2                                  	#Associate pin 24 to ECHO

print ("Distance measurement in progress")

wpi.pinMode(TRIG, wpi.OUTPUT)              	#Set pin as GPIO out
wpi.pinMode(ECHO, wpi.INPUT)              	#Set pin as GPIO in

try: 
	while True:
	
		wpi.digitalWrite(TRIG, wpi.LOW)          	 #Set TRIG as LOW
		print ("Waitng For Sensor To Settle")
		time.sleep(0.5)                          	 #Delay
		
		wpi.digitalWrite(TRIG, wpi.HIGH)         	 #Set TRIG as HIGH
		time.sleep(0.00001)                      	 #Delay of 0.00001 seconds
		wpi.digitalWrite(TRIG, wpi.LOW)          	 #Set TRIG as LOW
		
		while wpi.digitalRead(ECHO)== wpi.LOW:       #Check whether the ECHO is LOW
			pulse_start = time.time()              	 #Saves the last known time of LOW pulse
		
		while wpi.digitalRead(ECHO)== wpi.HIGH:      #Check whether the ECHO is HIGH
			pulse_end = time.time()                	 #Saves the last known time of HIGH pulse 
		
		pulse_duration = pulse_end - pulse_start 	 #Get pulse duration to a variable
		
		distance = pulse_duration * 17000        	 #Multiply pulse duration by 17150 to get distance
		distance = round(distance, 2)            	 #Round to two decimal points
		
		if distance > 2 and distance < 400:      	 #Check whether the distance is within range
			print ("Distance:",distance - 0.5,"cm")  #Print distance with 0.5 cm calibration
		else:
  			print ("Out Of Range")                   #display out of range
  		
except KeyboardInterrupt:
	print("Exit")
