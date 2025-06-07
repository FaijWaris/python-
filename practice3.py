#find all files and folders in a directory
import os

directory_path = "C:\Users\faijw\OneDrive\Desktop\New folder" # Use raw string for Windows paths
contents = os.listdir(directory_path)

for item in contents:
    print(item)
