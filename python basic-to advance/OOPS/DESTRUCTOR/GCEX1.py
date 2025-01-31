#GCEX1.py
import gc
print("Program execution strated")
print("Initially, is GC Running=",gc.isenabled())
a=10
b=20
c=a+b
gc.disable()
print("val of a=",a)
print("Now, is GC Running=",gc.isenabled())
print("val of b=",b)
gc.enable()
print("Sum=",c)
print("Now, is GC Running=",gc.isenabled())
print("Program execution ended")