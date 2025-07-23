s = input("Enter camelCase: ")

for c in s:
    if c == c.upper():
        print("_", end="")
    print(c.lower(), end="")
print()