import RPi.GPIO as GPIO
import time

import sys

def move_servo(pin_number, position, delay=2):
	GPIO.setmode(GPIO.BCM)

	GPIO.setwarnings(False)

	GPIO.setup(pin_number, GPIO.OUT)

	p = GPIO.PWM(pin_number, 50)
	p.start(8)

	try:
		mode = 11 #float(raw_input('Input:'))
		p.ChangeDutyCycle(position)
		time.sleep(delay)
		p.ChangeDutyCycle(8)

	except KeyboardInterrupt:
		GPIO.cleanup()
		print "Not a number"