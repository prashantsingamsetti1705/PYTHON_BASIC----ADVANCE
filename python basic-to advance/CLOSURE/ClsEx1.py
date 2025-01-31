#ClsEx1.py
def greet():
	sname="Rossum" # Local var in outer function
	LF=lambda : "Hi:"+sname
	return LF


xyz=greet() # Function Call
print("type xyz=",type(xyz))
res=xyz()
print(res)