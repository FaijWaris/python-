f=open("poem.txt")
data=f.read()
if("twinkle" in data):
    print("The word 'twinkle' is present in the poem.")
print(data)
f.close()