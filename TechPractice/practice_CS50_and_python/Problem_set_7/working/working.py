import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = []
    matches = re.search(r"^([1-9]|1[0-2]):?([1-9]|[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2]):?([1-9]|[0-5][0-9])? (AM|PM)$", s)
    if matches:
        list_el = s.split(" to ")
        for i in list_el:
            if ":" in i and "AM" in i:
                a,b = i.split(":")
                a = int(a)
                if a == 12 and b == "00 AM":
                    c = "00:00"
                else:
                    c = f"{a:02d}:{b[:-3]}"
                time.append(c)
            elif ":" in i and "PM" in i:
                a,b = i.split(":")
                if int(a) == 12 and b == "00 PM":
                    a = 12
                else:
                    a = int(a)+12
                c = f"{a:02d}:{b[:-3]}"
                time.append(c)
            elif ":" not in i and "AM" in i:
                a,b = i.split(" ")
                a = int(a)
                if a == 12:
                    c = "00:00"
                else:
                    c = f"{a:02d}:00"
                time.append(c)
            elif ":" not in i and "PM" in i:
                a,b = i.split(" ")
                if int(a) == 12:
                    a = 12
                else:
                    a = int(a)+12
                c = str(a)+":00"
                time.append(c)
        return f"{time[0]} to {time[1]}"
    else:
        raise ValueError



if __name__ == "__main__":
    main()