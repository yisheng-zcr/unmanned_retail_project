#This py file is used to create customer object
class Customer(object):
	"""Customer Class"""
	def __init__(self, Id, Purchase_history,Cart):
		super(Customer, self).__init__()
		self.Id=Id
		self.Purchase_history=Purchase_history
		self.Cart=Cart

	def myprint(self):
		print("Id is",self.Id)
		print("Purchase history is",self.Purchase_history)
		print("Cart is"self.Cart)

