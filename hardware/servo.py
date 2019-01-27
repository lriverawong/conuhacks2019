import RPi.GPIO as GPIO
import time

import sys
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

p = GPIO.PWM(4, 50)

try:
	while True:
		mode=float(raw_input('Input:'))
		p.start(2)
		p.ChangeDutyCycle(mode)
		p.stop()

except KeyboardInterrupt:
	GPIO.cleanup()
	print "Not a number"