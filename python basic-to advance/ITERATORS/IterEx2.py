#Program for Demonstrating the need of Iterators
#IterEx2.py
tpl=(10,20,30,40,50,60,"Rossum","Python")
print("Content of tuple=",tpl) # Here tpl object is called Iterable Object
print("Type of tpl=",type(tpl)) #  <class 'tuple>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(tpl)
print("Content of itrobj=",itrobj) # <tuple_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class 'tuple_iterator'>
print("--------------------------------------------")
print("Content of tuple Iterator by using while")
print("--------------------------------------------")
#extract the data from List Iterator
while(True):
	try:
		print(next(itrobj))
	except StopIteration:
		break

print("--------------------------------------------")
