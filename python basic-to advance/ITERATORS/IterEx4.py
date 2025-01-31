#Program for Demonstrating the need of Iterators
#IterEx4.py
fs1=frozenset({10,20,30,40,50,60,"Rossum","Python"})
print("Content of frozenset=",fs1) # Here fs1 object is called Iterable Object
print("Type of frozenset =",type(fs1)) #  <class 'frozenset'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(fs1)
print("Content of itrobj=",itrobj) # <set_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class set_iterator'>
print("--------------------------------------------")
print("Content of frozenset Iterator by using for loop")
print("--------------------------------------------")
#extract the data from List Iterator
for val in itrobj:
	print(val)
print("--------------------------------------------")