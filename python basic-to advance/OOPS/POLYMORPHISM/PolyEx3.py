#PolyEx2.py
class Circle(object):
    def draw(self): # Original Method
        print("Drawing Circle")
class Rect(Circle):
    def draw(self):# Overridden Method
        print("Drawing Rect")
class Square(Rect):
    def draw(self):# Overridden Method
        print("Drawing Square")
        Circle.draw(self)
        Rect.draw(self)
#Main Program
s=Square()
s.draw()