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
		print("Cart is",self.Cart)
	
	def Reset(self):
		self.Id=-1
		self.Purchase_history={}
		self.Cart={}
		print("This Infromation is Resetted")    

	def Add_to_history(self,New_record):    
		for new_item in New_record:
			if new_item in self.Purchase_history:
				self.Purchase_history[new_item]+=New_record[new_item]
			else:
				self.Purchase_history[new_item]=New_record[new_item]

	def Del_from_history(self,Del_Record):
		for del_item in Del_Record:
			if del_item in self.Purchase_history:
				self.Purchase_history.pop(del_item)

	def Add_to_cart(self,New_cart):
		for new_item in New_cart:
			if new_item in self.Cart:
				self.Cart[new_item]+=New_cart[new_item]
			else:
				self.Cart[new_item]=New_cart[new_item]

	def Del_from_cart(self,Del_cart):
		for del_item in Del_cart:
			if del_item in self.Cart:
				self.Cart.pop(del_item)

	def Settlement():
		for item in self.Cart:
			if item in self.Purchase_history:
				self.Purchase_history[item]+=self.Cart[item]
			else:
				self.Purchase_history[item]=self.Cart[item]
		self.Cart={}


	 	
		
