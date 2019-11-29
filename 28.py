#######################################
# PROGRAM:      printing pattern                                                                                                       
# PURPOSE:      to print # in required length                                                                                                        
# AUTHOR(s):    Rashmi D                                                                                                                     
# VERSION:      1.0                                                                                                                                   
# LAST REVISED: 29th NOV 2019                                                                                                                         
# PLATFORM:     python                                                                                                                   
# SYSTEM:       WINDOWS10                                                                                                                            
#######################################

for i in range(4):
    for j in range(4):
        print("#",end="")

    print()


for i in range(4):
    for j in range(i+1):
        print("#",end="")

    print()


for i in range(4):
    for j in range(4-i):
        print("#",end="")

    print()