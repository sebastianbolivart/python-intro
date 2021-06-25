class Person:
	"""An example class to hold a persons name and age"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return self.name + ' is ' + str(self.age)

	def birthday(self):
		print ('Happy birthday you were', self.age)
		self.age += 1;
		print('you are now', self.age)

	def calculate_pay(self, hours_worked):
		rate_of_pay = 7.50
		if self.age >= 21:
			rate_of_pay += 2.50
		return hours_worked * rate_of_pay

	def is_teenager(self):
		return self.age < 20

p1 = Person('John', 36)
p2 = Person('Phoebe', 21)
p3 = Person('Adam', 19)

pay = p2.calculate_pay(40)
print('Pay', p2.name, pay)

pay = p3.calculate_pay(40)
print('Pay', p3.name, pay)

del(pay)

teen = p2.is_teenager()
print(teen)

print('Class atributes')
print(Person.__name__)
print(Person.__module__)
print(Person.__doc__)
print(Person.__dict__)
print('Object atributes')
print(p1.__class__)
print(p1.__dict__)
