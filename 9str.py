name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))


#giving the string input

user_input = input("enter your name:")
meassage = "hello %s" % user_input

# meassage = f"hello {user_input}"
print(meassage)


#string formatting with multiple variables


name = input("enter your name:")
surname = input("enter your surname:")
age = input("enter age:")
meassage = "hello %s %s %s" % (name,surname,age)

meassage = f"hello {name}{surname}"
print(meassage)


name = "rashmi"
print("hi %s"%(name))

