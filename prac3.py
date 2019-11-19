#Accessing Values in Strings

var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])


x = "Hello World!"
print(x[:6]) 
print(x[0:6] + "Guru99")

#Python String replace() Method

oldstring = 'I like Guru99' 
newstring = oldstring.replace('like', 'love')
print(newstring)


#Using "join" function for the string
print(":".join("Python"))

print("h".join("Python"))


#Reversing String
string="12345"		
print("".join(reversed(string)))

#Split Strings

word="guru99 career guru99"		
print(word.split(' '))


#split r
word="guru99 career guru99"		
print(word.split('r'))

x = "Guru99"
xx= x.replace("Guru99","Python")
print(xx)


x = "Guru99"
x = x.replace("Guru99","Python")
print(x)