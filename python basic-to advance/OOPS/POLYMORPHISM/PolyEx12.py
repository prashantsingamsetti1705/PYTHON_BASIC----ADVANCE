#PolyEx12.py
class C1:
    def __init__(self): # Original Constructor
        print("C1--Default Constructor")
class C2:
    def __init__(self): # Original Constructor
        print("C2--Default Constructor")
class C3(C2,C1):
    def __init__(self): # Overridden Constructor
        print("C3--Default Constructor")
        super().__init__()
        C1.__init__(self)

#Main Program
o3=C3() # Object Creation---Makes the PVM to Call Constructor

