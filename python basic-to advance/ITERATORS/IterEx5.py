#Program for Demonstrating the need of Iterators
#IterEx4.py
d1={1:"Python",2:"C",3:"C++",4:"Java",5:"DSA"}
print("Content of Dict=",d1) # Here d1 object is called Iterable Object
print("Type of d1 =",type(d1)) #  <class 'dict'>
print("--------------------------------------------")
#To Convert Iterable object into Iterator Object, we use iter()
itrobj=iter(d1)
print("Content of itrobj=",itrobj) # <dict_iterator object at 0x000001C5C37DB400>
print("Type of itrobj=",type(itrobj)) # <class dict_keyiterator'>
print("--------------------------------------------")
print("Content of dict Iterator by using for loop")
print("--------------------------------------------")
k=next(itrobj)
print(k,d1.get(k))
k=next(itrobj)
print(k,d1.get(k))
k=next(itrobj)
print(k,d1.get(k))
#extract the data from List Iterator
print("--------------------------------------------")
for val in itrobj:
	print("{}-->{}".format(val,d1[val]))
print("--------------------------------------------")