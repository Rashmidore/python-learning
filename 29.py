#######################################
# PROGRAM:      printing pattern                                                                                                       
# PURPOSE:      to print # in required length                                                                                                        
# AUTHOR(s):    Rashmi D                                                                                                                     
# VERSION:      1.0                                                                                                                                   
# LAST REVISED: 29th NOV 2019                                                                                                                         
# PLATFORM:     python                                                                                                                   
# SYSTEM:       WINDOWS10                                                                                                                            
#######################################

nums = (9,12,14,16,24)

for num in nums:

    if num % 5 == 0:
        print(num)
        break
        
else:
     print("not found")
    