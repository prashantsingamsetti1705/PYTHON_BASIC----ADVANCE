#Program for Demonstrating ---It is not possible to apply on Non-Iterable Objects like int,float, bool,complex and NoneType
#IterEx8.py
a=100 
print("Content of a=",a) # Here a object is called Non-Iterable Object
print("Type of a =",type(a)) #  <class int'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
#itrobj=iter(a) ----------------TypeError: 'int' object is not iterable
