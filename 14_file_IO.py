# read
f = open("practice.txt", "r")
data = f.read() # read entire file
data = f.readline() # reads one line at a time
print(data)
print(type(data))
f.close()

# write
f = open("practice.txt", "w") # write mode
f.write("I am kenil")
f.close()

f = open("practice.txt", "a") # append mode, add in last
f.write("\nI am software engineer")
f.close()

# modes
# r => read
# w => write
# a => append
# r+ => read and overwrite, pointer start, no truncate
# w+ => read and overwrite,                truncate
# a+ => read and append, pointer end, no truncate

# with syntax (when use with syntax so don't need to close the file is make automatically)
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

with open("practice.txt", "w") as f:
    f.write("new data")

# delete
import os
os.remove("practice.txt")