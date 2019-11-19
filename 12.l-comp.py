temps =[231,323,210,240,-9999,0]

#new_temp = [temp/10 for temp in temps]
new_temp = [temp/10 for temp in temps if temp != -9999 and temp != 0]
print(new_temp)


# print only the integer values
temps = [99,'no data',95,94,'no data']

new_temp = [temp for temp in temps if not isinstance(temp,str)]

print(new_temp)


# print only the posive values

temps = [1,-2,3,-4,5,-6]

new_temp = [temp for temp in temps if temp >= 0]

print(new_temp)


#else-if comprehension

temps =[231,323,210,240,-9999,0]

#new_temp = [temp/10 for temp in temps]
new_temp = [temp/10 if temp != -9999 else 0 for temp in temps]
print(new_temp)


#print 0 instead of strings


temps = [99,'no data',95,94,'no data']

new_temp = [temp if not isinstance(temp,str) else 0 for temp in temps]

print(new_temp)
