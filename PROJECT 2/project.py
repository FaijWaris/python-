import random
n= random.randint(1, 100)
a=-1
guess=0
while (a!=n):
    guess+=1
    a=int(input("guess the no: "))

    if a>n:
        print("lower no. plz")
    elif a<n:
        print("higher no. plzz")
    else:
      break
print(f"you guessed it in {guess} tries")




