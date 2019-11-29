#######################################
# PROGRAM:      continue command                                                                                                       
# PURPOSE:      to print 1-100 and skip the values divisible by 3                                                                                                           
# AUTHOR(s):    Rashmi D                                                                                                                     
# VERSION:      1.0                                                                                                                                   
# LAST REVISED: 29th NOV 2019                                                                                                                         
# PLATFORM:     python                                                                                                                   
# SYSTEM:       WINDOWS10                                                                                                                            
#######################################

for i in range (1,101):
    
    if i%3==0 or i%5==0:
        continue
    print(i)