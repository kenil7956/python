slogan = "sparrow can never be a falcon"

# Reversed string by character
print(slogan[::-1])

# Reverse each word individually
split_variable = slogan.split()
print(split_variable)
print(split_variable[0][::-1], split_variable[1][::-1], split_variable[2][::-1], split_variable[3][::-1], split_variable[4][::-1], split_variable[5][::-1])

# Add * between two words
modified_slogan = slogan.replace(" ", " * ")
print(modified_slogan)

modified_slogan = " * ".join(slogan.split())
print(modified_slogan) 

# Replace "is" to "was"
my_str = "this is my string"
print(my_str.replace(" is ", " was "))

# interchange 2 letter
my_str = "this is my string"
new_str = my_str.split()
print(new_str)
print(new_str[0][0:2][::-1] + new_str[0][2:4][::-1], new_str[1][::-1], new_str[2][::-1], new_str[3][0:2][::-1] + new_str[3][2:4][::-1] + new_str[3][4:][::-1])