import time 
import os

while True:
    if os.path.exists("fruits.txt"):
        with open("fruits.txt") as file:
             print(file.read())
    else:
        print("file doesnot exits")

    time.sleep(10)



    