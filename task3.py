num = input("Enter a number: ")
digits = [int(x) for x in num]
i = 1
while i < len(digits) and digits[i] > digits[i - 1]:
    i += 1
if i == 1 or i == len(digits):
    print("Not a Hill Number")
else:
    while i < len(digits) and digits[i] < digits[i - 1]:
        i += 1
    if i == len(digits):
        print("Yep it is a Hill Number")
    else:
        print("Noooooooo")