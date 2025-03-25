# sets is mutable but set's element is immutable
# Sets are unordered, unchangeable*, and unindexed.

my_set = {1, 2, 3, 3} # repeated elements stored only once
print(my_set)

empty_set = set() # create empty sets
print(type(empty_set))

# Methods
my_set = {1, 2}

my_set.add(3)
my_set.add(4)
my_set.add(4)
my_set.add("hello")
my_set.add(("apple", "banana"))

my_set.remove(1) # does not exist, remove() will raise an error
my_set.discard(7) # does not exist, discard() will NOT raise an error

print(my_set)

my_set.clear()
print(len(my_set))

print(my_set.pop())
print(my_set.pop())
print(my_set.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1.intersection(set2))

