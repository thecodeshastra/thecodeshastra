U = input("Input: ")
V = U.strip()
l = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
for c in V:
    if c in l:
        continue
    else:
        print(c, end="")
print()