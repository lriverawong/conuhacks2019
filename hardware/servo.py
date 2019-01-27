import RPi.GPIO as GPIO
import time

import sys

def init():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4, GPIO.OUT)

	p = GPIO.PWM(4, 50)
	p.start(2)

def cleanup():
	GPIO.cleanup()

try:
	while True:
		mode=float(raw_input('Input:'))
		init()
		p.ChangeDutyCycle(mode)
		time.sleep(1)
		cleanup()

except KeyboardInterrupt:
	cleanup()
	print "Not a number"