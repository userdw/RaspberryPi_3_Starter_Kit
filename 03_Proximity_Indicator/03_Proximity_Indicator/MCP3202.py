#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import os
from time import strftime

CS = 4
CS2 = 7
CLK = 11
MOSI = 10
MISO = 9
LDAC = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(MOSI, GPIO.OUT)
GPIO.setup(CS2, GPIO.OUT)
GPIO.setup(LDAC, GPIO.OUT)
GPIO.setup(MISO, GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.output(CS, True)
GPIO.output(CLK, False)
GPIO.output(MOSI, True)

def myspi(rdata):
	dataX = 0
	mask = 0x80
	for i in range(8):
		if(rdata & mask):
			GPIO.output(MOSI, True)
		else:
			GPIO.output(MOSI, False)
		GPIO.output(CLK, True)
		if(GPIO.input(MISO) == 1):
			dataX = dataX + mask
		GPIO.output(CLK, False)
		mask = mask >> 1
	return dataX;

def readADC(ch):
	cmd = 0
	if ch == 0: cmd = 0x80 	 	
	elif ch == 1: cmd = 0xc0	
	#elif ch == 2: cmd = 0x00
	#elif ch == 4: cmd = 0x04
	GPIO.output(CS, False)
	a = myspi(0x01)
	#print "a: ",a
	b = myspi(cmd)
	#print "b: ",b
	c = myspi(0x00)
	#print "c: ",c 
	v = ((b & 0x0f) << 8) + c
	#print "v: ",v
	GPIO.output(CS, True)
	v = round(float(v), 2)
	#v=round(float(v)/4095*3.3,2)
	return v;

def setDAC(data, channel):
	cmd = 0
	if channel == 1: cmd = 0xF0
	else: cmd = 0x70

	GPIO.output(LDAC,False)
	GPIO.output(CS2,False)
	data = int(float(data * 4095 / 255))
	a = myspi((data >> 8) + cmd)
	b = myspi(data & 0xFF)
	GPIO.output(CS2, True)
	return;