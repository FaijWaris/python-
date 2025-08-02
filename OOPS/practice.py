class programmers:
    company="Microsoft"
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode =pincode
        print("Welcome to the team!")
p=programmers("Alice", 50000, 123456)
print(p.name, p.salary, p.pincode,p.company)  # Alice 50000 123456        