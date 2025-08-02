class empolyee:
 name="faij"
 language="python"
 def __init__(self,name,salary,language):#dunder method which is automatically called
   self.name=name
   self.salary=salary
   self.language=language
   print("iam good boy"  ) 
 def getinfo(self): # koi bhi method me hamseha self parameter pass karna hota hai
        print(f"{self.name} is a {self.language} developer")
 


faij=empolyee("shilpa",1000,"js")
print(faij.name,faij.language,faij.salary)  # faij