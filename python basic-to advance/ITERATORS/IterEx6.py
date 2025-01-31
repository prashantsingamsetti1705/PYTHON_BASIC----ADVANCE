#Program for Demonstrating the need of Iterators
#IterEx6.py
s="PYTHON"
print("Content of s=",s) # Here s object is called Iterable Object
print("Type of s =",type(s)) #  <class str'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(s)
print("Content of itrobj=",itrobj) # <str_ascii_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class 'str_ascii_iterator'>
print("--------------------------------------------")
print("Content of str_ascii_Iterator by using for loop")
#extract the data from str_ascii_Iterator
print("--------------------------------------------")
for val in itrobj:
	print(val)
print("--------------------------------------------")