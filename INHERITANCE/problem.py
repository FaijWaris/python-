class complex:
               def __init__(self, r, i):
                       self.r=r
                       self.i=i
               def __add__(self, other):  
                       return complex(self.r + other.r, self.i + other.i)     
               def __str__(self):
                       return f"{self.r} + {self.i}i"                
               
c1=complex(2, 3)
other=complex(4, 5)
print(c1 + other)









