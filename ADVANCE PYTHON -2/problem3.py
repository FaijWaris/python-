def divisible(n):
    if n%3==0:
        return True
    return False
l=[1,2,3,4,5,6,7,8,9]
a=filter(divisible,l)
print(list(a))