# d={} #empty dictionary
# s={}# dont use this bcz it create empty dictionary
# e=set() #empty set
# print(type(e)) #<class 'set'>

# s={1,1,12,3,4}
# print(s)  # {1, 3, 4, 12} - duplicates are removed

# #set methods
s={1, 2, 3, 4, 5,"faij"}
# print(s,type(s))  # {1, 2, 3, 4, 5, 'faij'} <class 'set'>
s.add(255)
# print(s,type(s))  
s1={1,2,3,4,}
s2={1,2,3,4,5}
print(s1.union(s2)) #pura mil jana
print(s1.intersection(s2))# common elements
print(s1.difference(s2))#s1 me jo hai s2 me nahi