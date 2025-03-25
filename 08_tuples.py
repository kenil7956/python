# Tuples is immutable

fruits = ("orange", "mango", "kiwi", "banana")
print(fruits[0])
print(fruits[1:3])
print(len(fruits))

fruits = ("apple",) # One item tuple

# Methods
fruits = ("orange", "mango", "kiwi", "banana", "mango")

print(fruits.count("mango"))
print(fruits.index("mango"))