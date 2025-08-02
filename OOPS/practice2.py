class claculator:
    def __init__(self, n):
        self.n=n
        

    def square(self):
       print(f"the square is {self.n**2}")  # Output: 16

    def squareroot(self):
        print(f"the square root is {self.n**0.5}")
       
    def cuberoot(self):
        print(f"the cube root is {self.n**(1/3)}")
       
    

user=claculator(4)
user.square()    # Output: 20

    