import sys
import csv

try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 4:
        sys.exit("Too many command-line arguments")
    elif "csv" not in sys.argv[1] and "csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    # elif sys.argv[1] != "before.csv":
    #     sys.exit(f"Could not read {sys.argv[1]}")
    else:
        lists = []
        list_name = []
        with open(sys.argv[1]) as F:
            reader = csv.DictReader(F)
            for R in reader:
                list_name.append(R["name"])
                for name in list_name:
                    string = name
                    A,B = string.split(", ")
                lists.append([A , B , R["house"]])


        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for append in lists:
                writer.writerow({"first": append[1], "last": append[0], "house": append[2]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")