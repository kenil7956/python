# Lists is mutable

student = ["smit", 22, 54.3, "ahmedabad"]
student[0] = "kenil"
print(student)
print(len(student))


# Methods
list = ["orange", "mango", "kiwi", "banana"]

list.append("mango") # Add
list.insert(1, "kiwi") # add in specified index

list.remove("mango") # removes the first occurrence
list.pop(1) # removes the specified index
list.pop() # removes the last item

list.sort() # sort the list alphanumerically, ascending
list.sort(reverse=True) # To sort descending

list.reverse() # Reverse the order

list2 = list.copy() # copy of a list

print(list)


# practice
# check if a list contains a palindrome of elements.
my_list = [1, 2, 3, 2, 1]
copy_list = my_list.copy()
copy_list.reverse()

if(my_list == copy_list):
    print("palindrome")
else:
    print("not palindrome")