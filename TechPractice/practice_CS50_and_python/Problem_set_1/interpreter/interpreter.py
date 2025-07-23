U = input("Enter your expression: ")
x, y, z = U.split(" ")
x = float(x)
z = float(z)
if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/" and z >= 1:
    print(x/z)
elif y == "/" and z == 0:
    print("Error Z can't be zero")