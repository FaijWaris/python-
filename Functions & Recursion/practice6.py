def remove():
    l=[1,2,3,4,5,]
    n=int(input("Enter a number to remove: "))
    if n in l:
        l.remove(n)
    else:   
      l.append(n)
    print(l)

remove()