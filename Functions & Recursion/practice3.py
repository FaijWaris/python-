def sum():
    n = int(input("Enter a number: "))
    if n==1:
        return 1
    add=n * (n+1)//2
    print(f"The sum of the first {n} natural numbers is {add}")
sum()    