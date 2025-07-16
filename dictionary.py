marks={
    "harry":1,
    "rohan":2,
}
# print(marks,type(marks))

#dict methods
print(marks.keys())  # returns keys
print(marks.values())  # returns values 
print(marks.items())  # returns key-value pairs
# print(marks.get("harry"))  # returns value for key "harry"
# print(marks.get("rohan"))  # returns value for key "rohan"


print(marks.get("harry3"))#its gives none if key is not present
print(marks["harry3"])#it will give error if key is not present

