import sys

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    elif "py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        count = 0
        with open(sys.argv[1]) as F:
            for line in F:
                line = line.lstrip(" ")
                if line.startswith("# ") or line == "\n":
                    continue
                else:
                    count += 1
            print(count)

except FileNotFoundError:
    print("File does not exist")