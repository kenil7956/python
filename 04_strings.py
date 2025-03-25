# Strings is immutable

# String Concatenation
a = "hello"
b = "guys"
c = a + b
print(c)

d = a + " " + b
print(d)
print(len(d)) # length

# Indexing
a = "apple" # [0 1 2 3 4]

# Slicing
a = "apple is good "
print(a[1:4])
print(a[-5:-2])
print(a[::-1]) # reverce string

# Modify
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("a", "j"))
print(a.split(","))

# Format Strings
age = 22
txt = "My name is kenil and i am " + age # not valid
print(txt)

age = 22
txt = f"My name is smit and i am {age}" # F-Strings
print(txt)

# Escape Characters
txt = "good morning\\ every\t budy\'\n how are\b you"
print(txt)

# String Methods
name = "smit"
print(name.capitalize())
print(name.endswith("s"))
print(name.find("m"))



# practice
str = "my name is kenil"
str2 = str.split(" ")
result = str2[0][::-1], str2[1][::-1], str2[2][::-1], str2[3][::-1] # , thi space kari sakay not use " "
print(str2)
print(result)
print(str[::-1])