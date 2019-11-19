def area (a,b):
    return a*b
print(area(4,5))




#program using *args

def fun(* args):
    return sum(args) / len(args)

print(fun(1,2,3,4,5))


#program using *kwargs

def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3,b=6))