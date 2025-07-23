def main():
    U = convert(input("Enter a time in 24-hour format : "))
    # print(U)
    if U >= 7 and U <= 8:
        print("breakfast time")
    elif U >= 12 and U <= 13:
        print("lunch time")
    elif U >= 18 and U <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.strip().split(":")
    hours = float(hours)
    minutes = float(minutes)/60
    return hours+minutes

if __name__ == "__main__":
    main()