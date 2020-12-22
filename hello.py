#! /usr/bin/python3
# print("Hello world")
# print('Hello, world')
# name = input('Enter your name: ')
# print('Hello', name)
# name = input('What is the name of your best friend: ')
# print('Hello Best Friend', name)
# name = input('es un care gueva')
print('Bienvenido a Arpanet')
password1 = input('Ingrese su identificador unico de acceso 1: ')
password2 = input('Ingrese su identificador unico de acceso 2: ')

id = (password1, ' ', password2)

print('El codigo ha sido aceptado', id)
print('---->Bienvenido a Arpanet<----')
z = """
	Hello
		world
"""
print(z)

var1 = "Sebastian"
var2 = int(3)
var3 = "true"

print("El string ", var1.upper(), "tiene ", len(var1), "caracteres")
print(type(var2))
print(type(var3))

my_string = 'Count, the number of     spaces'
print(my_string[5:])

print("*" * 10)
print("Hi" * 10)

title = 'The Good, The Bad, and the Ugly'

print('Source string', title)
print('Split using  a space')
print(title.split(' '))
print('Split using  a coma')
print(title.split(','))

print("my_string.count(' '):", my_string.count('o'))

welcome_message = 'Hello World, i am sebastian!'
print(welcome_message)
print(welcome_message.replace('Hello', 'Goodbye'))

format_string = 'Hello {}!'
print(format_string.format('phoebe'))

import string
template_sebastian = string.Template('$artist sang $song in $year')
print(template_sebastian.substitute(artist="Freddy Mercury", song="The Great Pretender", year="1982"))

exerecise1 = "enyse,Marie,Smith,21,London,UK"
print(exerecise1.replace(',',' '))
