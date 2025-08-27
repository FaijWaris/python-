class Animals():
    pass

class pets(Animals):
    pass
   
class dogs(pets):
   
    @staticmethod
    def barks():
        print("bow bow!")  
d=dogs()
d.barks()        

