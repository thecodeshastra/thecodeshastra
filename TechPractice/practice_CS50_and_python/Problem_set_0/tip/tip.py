def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    F = d.removeprefix("$")
    N = float(F)
    return N

def percent_to_float(p):
    # TODO
    F = p.removesuffix("%")
    M = float(F)/100
    return M

main()