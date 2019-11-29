#######################################################################################################################################################
# PROGRAM:      break command                                                                                                       #
# PURPOSE:      to break the while loop                                                                                                            #
# AUTHOR(s):    Rashmi D                                                                                                                     #
# VERSION:      1.0                                                                                                                                   #
# LAST REVISED: 29th NOV 2019                                                                                                                         #
# PLATFORM:     python                                                                                                                   #
# SYSTEM:       WINDOWS10                                                                                                                            #
#######################################################################################################################################################

av = 5

x = int(input("how many choc"))

i = 1
while i <= x:

    if i>av:
        print("stock empty")
        break

    print("candy")
    i=i+1     

#print("bye")   