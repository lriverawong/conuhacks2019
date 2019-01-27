from servo import move_servo
import sys

def classify_trash(class_type):
	move_servo(4,2, delay=1)
	move_servo(17,3)