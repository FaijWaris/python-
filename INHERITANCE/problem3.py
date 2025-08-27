class empolyee():
 salary = 234
 increment = 20
 @property
 def salaaryafterincrement(self):
       return self.salary + (self.salary * self.increment / 100) 

e=empolyee()
  
print(e.salaaryafterincrement)  # This will print the salary after increment, which is 0 in this case since salary is not set.








      