x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less or Equal")



if isinstance(x, int) or isinstance(x, float) or x=='1':
    print("Valid type!")
else:
    print("Not valid!")


def foo(password):
    if len(password) >= 8:
        return True
    else:
        return False

print(foo("rashdore"))



def foo(temperature):
    if temperature >= 7:
        return "warm"
    else:
        return "cold"

print(foo(8))



def check(value):
    if(value > 25):
        return "Hot"
    elif(25 >= value >= 15) :
        return "warm"
    else:
        return"clod"

print(check(13))

