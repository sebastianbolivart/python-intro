"""num = (int(input('Enter a number:')))
if num < 0:
	print (num, 'is negative')
else:
	print(num, 'is positive')

print('Program over')

print('-------------------------')
savings = float(input('Enter how much you have in savings: '))
if savings <= 0:
	print("Sorry no savings")
elif savings < 500:
	print('Well done')
elif savings < 1000:
	print('Thats a tidy sum')
elif savings < 10000:
	print('Welcome Sir!')
else:
	print('Thank you')"""

print('-----------Exercice 1--------------')

num1 = int(input('Insert a number please: '))

if num1 == 0:
	print('The inserted number is ', num1)
elif num1 > 0:
	print('The inserted number is positive')
elif num1 < 0:
	print('The inserted number is negative')
else:
	print('The inserted number is not a number')


print('-----------Exercice 2--------------')

num2 = int(input('Insert a number please: '))

if ((num2 % 2) == 0):
	print('El numero ', num2, ' es par')
else:
	print('El numero ', num2, ' no es par')	