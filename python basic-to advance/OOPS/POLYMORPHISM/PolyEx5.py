#PolyEx5.py
class Circle:
    def draw(self): # Original Method
        print("Drawing Circle")
class Rect:
    def draw(self):# Original Method
        print("Drawing Rect")
class Square(Rect,Circle):
    def draw(self):# Overridden Method
        print("Drawing Square")
        Rect.draw(self)
        Circle.draw(self)

#Main Program
s=Square()
s.draw()