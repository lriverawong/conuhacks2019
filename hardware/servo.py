import RPi.GPIO as GPIO
import time

import sys

def move_servo(pin_number, position):
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(pin_number, GPIO.OUT)

	p = GPIO.PWM(pin_number, 50)
	p.start(8)

	try:
		mode = 11 #float(raw_input('Input:'))
		p.ChangeDutyCycle(position)
		time.sleep(2)
		p.ChangeDutyCycle(8)

	except KeyboardInterrupt:
		GPIO.cleanup()
		print "Not a number"