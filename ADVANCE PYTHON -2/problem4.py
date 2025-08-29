from functools import reduce
a=[1,22,3,3,444,4444]
def greater(a,b):
    if a>b:
        return a
    return b    
g=reduce(greater,a)
print(g)