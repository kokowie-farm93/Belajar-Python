# Search for a letter in a word
word = input("Enter a word: ")
lettter_to_find = input("Enter letter to search: ")

for letter in word:
    if letter == lettter_to_find:
        print(f"Letter", {lettter_to_find}, "found in word!")
        break
else:
        print(f"Letter", {lettter_to_find}, "not found")