from functools import reduce
#MAP example
l=[1,2,3,4,5]
# square=lambda x:x*x
# a=map(square,l)
# print(list(a))


#filter example
def even(n):
    if (n%2==0):
        return True
    return False
a=filter(even,l)
print(list(a))

#REDUCE EXAMPLE
def sum(a,b):
    return a+b  
s=reduce(sum,l)
print(s)