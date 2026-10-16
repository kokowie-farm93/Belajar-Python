# SET is unordered = no fixed order, no index, unique values, no duplicates

fruits = {"pineapple", "apple", "avocado"}
print(fruits)

fruits.add("mango")
print(fruits)

fruits.add("mango")
print(fruits)

fruits.remove("apple")
print(fruits)

for x in fruits:
    print(x)