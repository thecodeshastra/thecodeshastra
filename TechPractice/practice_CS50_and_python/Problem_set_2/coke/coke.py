def main():
    pass
    A = "Amount Due: "
    Aa = 50
    B = "Change Owed: "
    coin_cal(A, Aa, B)

def coin_cal(a, c, b):
    while c > 0:
        print(a + str(c))
        U = int(input("Insert coin: "))
        if U == 25:
            c = c-25
        elif U == 10:
            c = c-10
        elif U == 5:
            c = c-5
        else:
            continue
    if c <= 0:
        print(b + str(-c))

main()