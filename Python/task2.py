word = input("Enter a string: ")
sorted_word =sorted(word)
print(sorted_word)
for char in sorted(set(sorted_word)):
    print(char, word.count(char))