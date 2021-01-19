def print_msg(msg):
    print(msg)

print_msg("Hola mundo, como estas!!")


def square(n):
	return n * n

print (square(2))

def greeter(name, message = 'live long and prosper'):
	print('Welcome', name, '-', message)
greeter('Eloise')
greeter('Eloise', 'Hope you like Python')

def greeter(name, title = 'Dr', prompt = 'Welcome', message = 'Live Long and Prosper'):
	print(prompt, title, name, '-', message)
greeter(message = 'We like Python', name = 'Lloyd')

double = lambda i : i * i 

print(double(10))