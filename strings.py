name="faij"#strings are immutable
#slicing in string
name2="borker"
print(name2[0:3]) # prints 'bor' because it slices from index 0 to 2 and last index is excluded

#when we print 
print(name[:3]) # prints 'fai' because it slices from index 0 to 2 and last index is excluded
#and when we print 
print(name[1:]) # prints 'aij' because it slices from index 1 to the end of the string


#skiip value in string
a="0123456789"
print(a[1:7:3])

#string function
#lenth function
print(len(name))
#endswith,startgswith
print(name.endswith("ij"))
print(name.startswith("fa"))
#capatilize
                                                                