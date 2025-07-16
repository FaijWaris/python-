#greater of four no.
a=int(input("enter the no1:"))
b=int(input("enter the no2:"))
c=int(input("enter the no3:"))
d=int(input("enter the no4:"))

if(a>b and a>c and a>d):
    print("a is greater")
elif(b>a and b>c and b>d):
    print("b is greater")
elif(c>a and c>b and c>d):
    print("c is greater")
elif(d>a and d>b and d>c):
    print("d is greater")
else:
    print("all are equal")