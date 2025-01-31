#Program for Demonstrating the need of Iterators
#IterEx1.py
lst=[10,20,30,40,50,60,"Rossum","Python"]
print("Content of lst=",lst) # Here lst object is called Iterable Object
print("Type of lst=",type(lst)) #  <class 'list'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(lst)
print("Content of itrobj=",itrobj) # <list_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class 'list_iterator'>
print("--------------------------------------------")
print("Content of List Iteratorby using while")
print("--------------------------------------------")
#extract the data from List Iterator
print(next(itrobj))
print(next(itrobj))
print(next(itrobj))
while(True):
	try:
		print(next(itrobj))
	except StopIteration:
		break

print("--------------------------------------------")
lst1=["Rossum","Travis","Dennis","Java"]
itrobj1=iter(lst1)
print("Content of lst1=",lst1) # Here lst object is called Iterable Object
print("Type of lst1=",type(lst1)) #  <class 'list'>
print("--------------------------------------------")
print("Content of itrobj1=",itrobj1) # <list_iterator object at 0x000001C5C37DB400>
print("Type of itrobj1=",type(itrobj1)) # <class 'list_iterator'>
print("--------------------------------------------")
print("Content of List Iteratorby using for loop")
print("--------------------------------------------")
for val in itrobj1:
	print(val)
print("--------------------------------------------")