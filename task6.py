def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not anagram")