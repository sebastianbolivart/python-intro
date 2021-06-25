class Account:
	"""A class that represents a client bank account"""
	def __init__ (self, accountNumber, accountHolder, openingBalance, accountType):
		self.accountNumber 	= accountNumber
		self.accountHolder 	= accountHolder
		self.openingBalance = openingBalance
		self.accountType 	= accountType
		self.balance 		= self.openingBalance

	def deposit(self, amount):
		self.balance = self.openingBalance + amount
		#return self.balance

	def withdraw(self, amount):
		self.balance = self.balance - amount
		#return self.balance

	def get_balance(self):
		return self.balance


acc1 = Account('123', 'John', 10.05, 'current')
acc2 = Account('345', 'John', 23.55, 'savings')
acc3 = Account('567', 'Phoebe', 12.45, 'investment')

print(acc1.accountHolder)
print(acc2.accountHolder)
print(acc3.accountHolder)

acc1.deposit(23.45)
acc1.withdraw(12.33)
print('Balance:', acc1.get_balance())