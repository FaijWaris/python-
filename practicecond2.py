a=int(input("enter subject 1 marks:"))
b=int(input("enter subject 2 marks:"))
c=int(input("enter subject 3 marks:"))

total_percantage=(a+b+c)/300*100
print("total percentage is:",total_percantage)
if(total_percantage>=40):
    print("you are pass")
elif(total_percantage<40 and total_percantage>=33):     
    print("you are pass with grace marks")
else:   
    print("you are fail")