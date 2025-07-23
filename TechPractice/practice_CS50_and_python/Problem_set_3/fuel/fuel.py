def main():
    while True:
        try:
            U = input("Fraction: ")
            x, y = U.split("/")
            x = int(x)
            y = int(y)
            if x > y:
                continue
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            break
    calc(x,y)

def calc(a,b):
    Z = (a/b)*100
    Z = round(Z)
    if Z <= 1:
        print("E")
    elif Z >= 99:
        print("F")
    else:
        print(str(Z) + "%")

main()