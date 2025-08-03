class employee:#base class
   company= "Google"
   def show(self):
      print(f"Employee Name: {self.name}, Salary: {self.salary}")
# class programmer:
#    company= "Microsoft"
#    def show(self):
#       print(f"Employee Name: {self.name}, Salary: {self.salary}")

#    def showlanguage(self):
#       print(f"Employee Name: {self.name}, language: {self.language}")
class programmer(employee):# Inheriting from employee class
   company= "Microsoft"
def show(self):
     print(f"Employee Name: {self.name}, Salary: {self.salary}")
a=employee()
b=programmer()
print(a.company,b.company)