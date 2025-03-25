char = input("Enter character: ")

if(char == "a"):
    print("you have enter", char)
elif(char == "b"):
    print("you have enter", char)
elif(char == "c"):
    print("you have enter", char)
else:
    print("Invalid character")



num = int(input("Enter a number: "))

if(num > 0):
    if(num % 2 != 0):
        result = num + num
        print("you enter possitive odd number and its addition is", result)
    else:
        result = num * num
        print("you enter possitive even number and its multiplication is", result)
elif(num < 0 ):
    if(num % 2 != 0):
        result = num - num
        print("you enter negative odd number and its subtraction is", result)
    else:
        result = num / num
        print("you enter negative even number and its division is", result)
else:
    print("Number is zero")



marks = int(input("Enter marks: "))

if(marks > 100):
    print("Invalid marks")
elif(marks >= 90 ):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grede B")
elif(marks >= 60 and marks < 80):
    print("grade C")
elif(marks >= 40 and marks < 60):
    print("grade D")
else:
    print("fail")