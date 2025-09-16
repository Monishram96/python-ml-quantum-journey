##FILE HANDLING##
### WRITING TO A FILE ###

with open("sample.txt","w") as f:
    f.write("Hello,this is Day 5!\n")
    f.write(" File handling in python is easy.\n")



### READING THE FILE ###
with open("sample.txt","r") as f:
    content=f.read()
    print("File Content:\n",content)


### APPENDING THE LINE ###
with open("sample.txt","a") as f:
    f.write("this line is appended./n")
print("File operation is completed")
