# 1
# 1 1
# 1 1 1
# 1 1 1 1
# 1 1 1 1 1
n = int(input("Number of rows: "))
for i in range(1, n + 1): 
    print(i * "1 ")



# 1
# 2 3
# 4 5 6
# 7 8 9 10
num = 1
rows = 4
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()



# * * * * * 
# * * * *
# * * *
# * *
# *
for i in range(5, 0, -1):
    print(i * "* ")



#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# method 1
rows = 5
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("* ", end="")
    print()

# method 2    
rows = 5  
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)



#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# method 1
rows = 5  

# Upper half
for i in range(1, rows + 1):  
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

# Lower half
for i in range(rows - 1, 0, -1):  
    for j in range(rows - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()


# method 2 
rows = 5 

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)



# Factorial using while loop
num = int(input("Enter a number: "))
factorial = 1
i = num

while i > 1:
    factorial *= i
    i -= 1
print("factorial is", factorial)