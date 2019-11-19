myfile = open("fruits.txt")
#print(myfile.read())


# to print the content as many times you want


myfile = open("fruits.txt")
content = myfile.read()

myfile.close()

#print(content)


def foo(character, filepath="fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count()
    


