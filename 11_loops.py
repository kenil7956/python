# used to repeat instruuctions

# Python has two primitive loop commands:
# 1. while
# 2. for

# while
# sytax
while (condition):
    # statement
# rest of the code

i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i <= 10:
    print(i)   
    if(i == 5):
        break
    i += 1

i = 0 
while i <= 10:
    if(i == 5):
        i += 1
        continue # skip
    print(i)
    i += 1



# for (used for sequential traversal, For list, string, tuples etc.)
# syntax
sequence = "list, string, tuples etc."
for var in sequence:
    # statements
# rest of the code 

numbers = [1, 2, 3, 4, 5]
str = "kenil"
tup = (1, 2, 3, 4, 5, 6)
for val in tup:
    print(val)

for i in range(10): # range(stop)
    print(i)

for i in range(2, 10): # range(start, stop)
    print(i)

for i in range(2, 10, 2): # range(start, stop, step)
    print(i)

for i in range(5):
    pass # empty like no work

print("some work")    