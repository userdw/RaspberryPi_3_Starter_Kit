import MCP3202, time, datetime, os
from time import strftime


try:
  while 1:
    	os.system('clear')
	value1= MCP3202.readADC(0)	# range data 0 - vref (volt)
	voltage=round(float(value1*3300/4096),2)
	temperature = (voltage-500)/10
	tampil= round(float(temperature),2)
 	print "Weather Station"
	print "Curent Temperature : ",tampil,u"\u2103"
    	print ""
	print "Press CTRL+C to exit"
   	time.sleep(0.075)

except KeyboardInterrupt:
    	print "exit"

