#we use file bcz to store the data ,RAM are volitle it store data
#temporily but ,HDD AND SSD are non volitile which persist the data  which means the can store the data ,in compare to RAM the are slow
# there are mainly two types of files 1]text files 2]binary files
f=open("FILE/file.txt")
data=f.read()
print(data)
f.close() 