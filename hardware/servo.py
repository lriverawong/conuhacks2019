import RPi.GPIO as GPIO
import time

import sys

class Servo:
	def __init__(self):
		self.init_GPIO()

	def init_GPIO(self):
		GPIO.setmode(GPIO.BCM)

		GPIO.setup(4, GPIO.OUT)

		self.p = GPIO.PWM(4, 50)
		self.p.start(2)

	def cleanup(self):
		GPIO.cleanup()

	def change_duty_cycle(self, mode):
		self.p.ChangeDutyCycle(mode)

s = Servo()

try:
	while True:
		mode=float(raw_input('Input:'))
		s.init_GPIO()
		s.change_duty_cycle(mode)
		time.sleep(1)
		s.cleanup()

except KeyboardInterrupt:
	cleanup()
	print "Not a number"