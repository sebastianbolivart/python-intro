import random
number_to_guess = random.randint(1,10)

print('Welcome to the guess number game')

guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
	print('Sorry wrong number')
	guess = int(input('Please guess again: '))