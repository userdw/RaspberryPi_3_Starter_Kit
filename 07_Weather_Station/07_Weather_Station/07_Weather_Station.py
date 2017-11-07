import MCP3202
import time
import datetime
import os
from time import strftime

try:
	while 1:
    		os.system("clear")
		value1= MCP3202.readADC(0)
		voltage = round(float(value1 * 5000 / 4096), 2)
		temperature = (voltage - 550) / 10
		tampil = round(float(temperature), 2)
 		print("Weather Station")
		print("Curent Temperature : ", tampil, u"\u2103", "C")
    		print("")
		print("Press CTRL+C to exit")
   		time.sleep(0.075)

except KeyboardInterrupt:
	print("exit")
