#PolyEx2.py
class Circle(object):
    def draw(self): # Original Method
        print("Drawing Circle")
        #super().draw()--AttributeError draw() does not exist in object class.
class Rect(Circle):
    def draw(self):# Overridden Method
        print("Drawing Rect")
        super().draw()
class Square(Rect):
    def draw(self):# Overridden Method
        print("Drawing Square")
        super().draw()
#Main Program
s=Square()
s.draw()