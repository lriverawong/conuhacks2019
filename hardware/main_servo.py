from servo import move_servo

def classify_trash(class_type):
	if class_type == 0:
		move_servo(4,9, delay=1)
		move_servo(17,9.5)
		move_servo(4,8)
		move_servo(17,7.5)

	elif class_type == 1:
		move_servo(4,4, delay=1)
		move_servo(17,11.5)
		move_servo(17,8)
	elif class_type == 2:
		move_servo(4,6, delay=1)
		move_servo(17,11.5)
		move_servo(17,8)
	else:
		move_servo(17,3.5)
		move_servo(17,8)
