import RPi.GPIO as GPIO
import time

import sys

def move_servo(mode):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4, GPIO.OUT)

	p = GPIO.PWM(4, 50)
	p.start(2)
	p.ChangeDutyCycle(mode)
	GPIO.cleanup()

try:
	while True:
		mode=float(raw_input('Input:'))
		move_servo(mode)

except KeyboardInterrupt:
	GPIO.cleanup()
	print "Not a number"
