menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

amt = 0.00
while True:
    try:
        U = input("Item: ")
        A = U.lower().title()
        amt = float(amt)
        amt = amt + menu[A]
        round(amt, 2)
        if A in menu:
            print(f"Total: ${amt}0")
    except EOFError:
        print()
        break
    except KeyError:
        continue
    else:
        continue

