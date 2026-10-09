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
