#PolyEx1.py
class Circle:
    def draw(self): # Original Method
        print("Drawing Circle")

class Rect(Circle):
    def draw(self):# Overridden Method
        print("Drawing Rect")
        super().draw() # Calling super Class original method from Derived Class Overridden Method

#Main Program
print("w.r.t Rect class")
r=Rect()
r.draw()