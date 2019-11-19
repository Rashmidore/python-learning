#opening file using with comment

with open("fruits.txt") as myfile:
    content = myfile.read()
#print(content)


#to read the file in other directory

with open("fruits.txt","w") as myfile:
    content = myfile.write("papaya\ncoco\n")
#print(content)


#appending and read

with open("fruits.txt","a+") as myfile:
     myfile.write("oreo\n")

     myfile.seek(0)
     content = myfile.read()

print(content)

