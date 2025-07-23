def main():
    U = input("Fraction: ")
    A = convert(U)
    print(gauge(A))

def convert(fraction):
    while True:
        x, y = fraction.split("/")
        try:
            x = int(x)
            y = int(y)
            z = x/ y
            if x > y:
                fraction = input("Fraction: ")
                continue
            else:
                R = int(z * 100)
                return R
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")
            continue

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()