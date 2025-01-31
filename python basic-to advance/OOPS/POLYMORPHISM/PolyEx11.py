#PolyEx11.py
class C1:
    def __init__(self): # Original Constructor
        print("C1--Default Constructor")
class C2(C1):
    def __init__(self): # Overridden Constructor
        super().__init__()
        print("C2--Default Constructor")

class C3(C2):
    def __init__(self): # Overridden Constructor
        super().__init__()
        print("C3--Default Constructor")

#Main Program
o3=C3() # Object Creation---Makes the PVM to Call Constructor

