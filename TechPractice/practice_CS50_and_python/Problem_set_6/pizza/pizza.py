import sys
import csv
import tabulate

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    elif "csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        lists = []
        with open(sys.argv[1]) as F:
            reader = csv.reader(F)
            for R in reader:
                lists.append(R)
        header = lists[0]
        items = lists[1:]
        table = tabulate.tabulate(items, header, tablefmt="grid")
        print(table)
except FileNotFoundError:
    sys.exit("File does not exist")