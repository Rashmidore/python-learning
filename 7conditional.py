def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)

    else:
        the_mean = sum(value) / len(value)

    return the_mean

temp = {"mon":8,"tue":6,"wed":9}

date = (11,12,13,14)

print(mean(date))

print(mean(temp))



if isinstance(x, int) or isinstance(x, float) or x=='1':
    print("Valid type!")
else:
    print("Not valid!")