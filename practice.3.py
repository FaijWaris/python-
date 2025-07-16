p1="make a lot of money"
p2="make a lot of honey"
p3="make a lot of goney"

message=input("enter the comment :")
if(p1 in message or p2 in message or p3 in message):
    print("spam")
else:       
    print("not spam")