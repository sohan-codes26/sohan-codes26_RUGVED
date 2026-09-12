s = input("Enter string: ")
n = int(input("Enter n: "))
if len(s) % n != 0:
    print("Division not possible")
else:
    first = s[0:n]
    same = True
    for i in range(0, len(s), n):
        part = s[i:i+n]

        if part != first:
            same = False
    if same:
        for i in range(0, len(s), n):
            print(s[i:i+n])
    else:
        print("Sequence is not the same")