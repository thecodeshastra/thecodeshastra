import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    matches = re.split(r"\W+", s)
    for i in matches:
        if i.lower() == "um":
            count += 1
    return count


if __name__ == "__main__":
    main()