L = {}
while True:
    try:
        U = input()
        U = U.upper()
        if U in L:
            L[U] = L[U] + 1
        else:
            L[U] = 1
        # print(L)
    except EOFError:
        print()
        for i in sorted(L.keys()):
            print(L[i], i)
        break
    else:
        continue