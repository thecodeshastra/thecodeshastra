month =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    U = input("Date: ")
    try:
        if "/" in U:
            M,D,Y = U.split("/")
            M = int(M)
            D = int(D)
            Y = int(Y)
            if M > 0 and M < 13 and D > 0 and D < 32 and Y < 9999 and Y > 1000:
                print(f"{Y}-{M:02}-{D:02}")
                break
        elif "," in U:
            U = U.replace(",", "")
            M,D,Y = U.split(" ")
            D = int(D)
            Y = int(Y)
            # for i in month:
            #     if i == M:
            #         Mm = i+1
            #         print(Mm)
            if M in month:
                M = month.index(M)+1
            M = int(M)
            if  M > 0 and M < 13 and D > 0 and D < 32 and Y < 9999 and Y > 1000:
                print(f"{Y}-{M:02}-{D:02}")
                break
    except ValueError:
        continue
    except EOFError:
        print()
        break
    else:
        continue
