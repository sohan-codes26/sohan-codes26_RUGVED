def caesar_cipher(text, shift):
    result = ""
    for ch in text:
        result = result + chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
    return result
text = input("Enter text: ")
shift = int(input("Enter shift: "))
print(caesar_cipher(text, shift))