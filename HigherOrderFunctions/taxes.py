import math

def simple_tax_calculator(amount):
	return math.ceil(amount * 0.3)

def calculate_tax(salary, func):
	return func(salary)

salary = int(input('¿Cual es su salario? '))

print(calculate_tax(salary, simple_tax_calculator))