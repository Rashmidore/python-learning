
# we can redeclare the variables 
f = 0
print(f)

f = 2

print(f)

a = "guru"
b = 99
print(a+str(b))

# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
# global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)