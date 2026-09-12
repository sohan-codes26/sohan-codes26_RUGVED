text = input("Enter text: ")
letters = 0
words = len(text.split())
sentences = 0
for ch in text:
    if ch.isalpha():
        letters = letters + 1
    if ch == '.' or ch == '!' or ch == '?':
        sentences = sentences + 1
L = letters / words * 100
S = sentences / words * 100
grade = 0.0588 * L - 0.296 * S - 15.8
print("Grade level:", round(grade))