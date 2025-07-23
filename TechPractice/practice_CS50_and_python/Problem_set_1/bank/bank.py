U = input("Enter your word: ")
V = U.lower().strip()
W = U.lower().split()
if V.startswith("hello"):
    print("$0")
elif W[0].startswith("h"):
    print("$20")
else:
    print("$100")