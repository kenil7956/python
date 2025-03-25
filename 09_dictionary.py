# used to store data values in key:value pairs
# dictionaries are unordered, mutable(changeable) and do not allow duplicates

info = {
    "name": "kenil",
    "age": 22,
    "marks": 79.56,
    "subjects": ["maths", "physics", "chemistry"],
    "hobby": ("traveling", "learning"),
    "is student": True
}

print(info)
print(info["name"]) # Access but throw error
print(len(info))

empty_dict = {} # create empty dictionary

# Methods

print(info.keys())
print(info.values())
print(info.items())
print(info.get("name")) # Access but give None
print(info.update({"city": "ahmedabad"}))
print(info.pop("age")) # remove
print(info)

copy_info = info.copy()
print(copy_info)