def luhn(number):
    total = 0
    double = False
    for i in range(len(number) - 1, -1, -1):
        digit = int(number[i])
        if double:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total = total + digit
        double = not double
    if total % 10 == 0:
        return True
    else:
        return False
number = input("Enter card number: ")
if luhn(number):
    print("Valid")
else:
    print("Invalid")