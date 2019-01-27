import RPi.GPIO as GPIO
import time

import sys
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

p = GPIO.PWM(4, 50)
p.start(8)

try:
	while True:
		mode=float(raw_input('Input:'))
		p.ChangeDutyCycle(mode)
		time.sleep(2)
		p.ChangeDutyCycle(8)

except KeyboardInterrupt:
	GPIO.cleanup()
	print "Not a number"