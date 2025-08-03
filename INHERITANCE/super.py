class empolyee:
    def __init__(self):
        print("constructor of empolyee")
    a=1
class programmer(empolyee):
    def __init__(self):
        print("constructor of programmer")
    b=2    
class manager(programmer):
    def __init__(self):
        super().__init__() #ye apn tb chate hai ki upr wale ke bhi constructor chle
        print("constructor of manager")
    c=3
o=manager()
print(o.a,o.b,o.c)