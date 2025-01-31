#Program for Demonstrating the need of Iterators
#IterEx3.py
s1={10,20,30,40,50,60,"Rossum","Python"}
print("Content of set=",s1) # Here s1 object is called Iterable Object
print("Type of set=",type(s1)) #  <class 'set'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(s1)
print("Content of itrobj=",itrobj) # <set_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class set_iterator'>
print("--------------------------------------------")
print("Content of set Iterator by using for loop")
print("--------------------------------------------")
#extract the data from List Iterator
for val in itrobj:
	print(val)
print("--------------------------------------------")
