try:
    a=int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
finally:
    print("Input was successful.") #excute hoga hi chaye upr return hi kyu n ho
    