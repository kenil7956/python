light = "black"

if(light == "red"):
    print("stop") # indentation (space 4 tab) 
elif(light ==  "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")



marks = int(input("Enter student marks: "))

if(marks >= 90):
    print("A")
elif(marks >=80 and marks < 90):
    print("B")
elif(marks >=70 and marks < 80):
    print("C")
else:
    print("D")



# ODD OR EVEN
num = int(input("Enter number: "))

rem = num % 2 

if(rem == 0):
    print("EVEN")
else:
    print("ODD")