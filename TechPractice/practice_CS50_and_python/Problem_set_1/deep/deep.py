U = input("Enter user: ")

V = U.lower().strip()
if V == "42" or V == "forty two" or V == "forty-two":
    print("Yes")
else:
    print("No")