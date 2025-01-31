#Program for Demonstrating the need of Iterators
#IterEx7.py
r=range(10,21,2)
print("Content of r=",r) # Here r object is called Iterable Object
print("Type of r =",type(r)) #  <class range'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(r)
print("Content of itrobj=",itrobj) # <range_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class 'range_iterator>
print("--------------------------------------------")
print("Content of range__Iterator by using for loop")
#extract the data from range_Iterator
print("--------------------------------------------")
for val in itrobj:
	print(val)
print("--------------------------------------------")