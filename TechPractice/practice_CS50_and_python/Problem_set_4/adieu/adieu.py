import inflect

p = inflect.engine()
L = []
while True:
    try:
        U = input("Name: ")
        if U not in L:
            L.append(U)
    except EOFError:
        print()
        final = p.join(L)
        print(f"Adieu, adieu, to {final}")
        break
    else:
        continue
