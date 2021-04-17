print('Simple Calculator App')

def add(x, y):
	"""Adds two numbers"""
	return x + y

def substract(x, y):
	"""Substracts two numbers"""
	return x - y

def multiply(x, y):
	"""Multiplies two numbers"""
	return x * y

def divide(x, y):
	"""Divides two numbers"""
	return x / y

def check_if_user_has_finished():
	ok_to_finish = True
	user_imput_accepted = False

	while not user_imput_accepted:
		user_imput = input('Do you want to finish (y/n): ')
		if user_imput == 'y':
			user_imput_accepted = True
		elif user_imput == 'n':
			ok_to_finish = False
			user_imput_accepted = True
		else:
			print('Response must be (y/n), please try again')
	return ok_to_finish
	
