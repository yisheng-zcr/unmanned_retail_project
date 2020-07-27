import customer_model as customer

dict1={
	"milk":1,
	"sugar":2
}
dict2={
	"shoe":3
}

obj1=customer.Customer(1,dict1,dict2)
obj1.myprint()
#obj1.Reset()
New_record={
	"Coke":1
}
obj1.Add_to_history(New_record)
obj1.myprint()
obj1.Del_from_history(New_record)
obj1.myprint()

New_cart={
	"apple":1
}

obj1.Add_to_cart(New_cart)
obj1.myprint()
obj1.Del_from_cart(New_cart)
obj1.myprint()