import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

p = GPIO.PWM(4, 50)
p.start(2)

try:
	while True:
		p.ChangeDutyCycle(7.5)
		time.sleep(1)
		p.ChangeDutyCycle(12.5)
		time.sleep(1)
		p.ChangeDutyCycle(2.5)
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()
print("end of program")
