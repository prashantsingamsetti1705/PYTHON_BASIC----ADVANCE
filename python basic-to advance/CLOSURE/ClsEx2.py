#ClsEx2.py
def calculate(): # outer function
	num=1
	def inner_func(): # Inner function
		nonlocal num
		num=num+2
		return num
	return inner_func

#main Program
inner=calculate() # outer function call
print(inner()) # 3
print(inner()) # 5
print(inner()) # 7
print("-----------------------------------------------")
inner1=calculate() # outer function call
print(inner1())
print(inner1())