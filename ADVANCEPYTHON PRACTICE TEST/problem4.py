try:
    a=int(input("Enter a number: "))
    b=int(input("Enter b number: "))
    print(a/b)
except ZeroDivisionError as e:
    print("hey you cant divide a number by zero")        