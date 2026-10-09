fruits = ["apple", "avocado", "watermelon"]
print(fruits)

# Want just one item?
print(fruits[0])   # 0 is the first fruit
print(fruits[1])

# add another item
fruits.append("banana")
print(fruits)

# how many items?
print(f"Total fruits : {len(fruits)}")

# change an item
name = ["orange", "strawberry", "kiwi"]
print(name)
name[1] = "grape"
print(name) # ['orange', 'grape', 'kiwi']

# remove an item
name.remove("orange")
print(name)

# remove with del
del name[0]
print(name)

#count item
item = ["hat", "shoes", "chair"]
print(len(item))

color = ["black", "blue", "yellow", "green"]
print(color)
background_color = ["white", "purple", "gold"]
print(background_color)

set_color = color + background_color
print(set_color)

# loop for
for color in set_color:
    print(color) 
# or
for i in range(0, len(set_color)):
    print(set_color[i])

if "brown" in set_color:
    print("There is Brown")
else:
    print("Nothing")
