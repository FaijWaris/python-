class employee:#base class
   company= "Google"
   def show(self):
      print(f"Employee Name: {self.name}, Salary: {self.salary}")
class coder:
    language="python"
    def printlanguage(self):
        print(f"Employee Language: {self.language}")
class programmer(employee,coder):# Inheriting from employee class
   company= "Microsoft"
def show(self):
     print(f"Employee Name: {self.name}, Salary: {self.salary}")
a=employee()
b=programmer()
b.printlanguage()