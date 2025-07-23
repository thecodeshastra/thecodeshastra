import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if "youtube" not in s:
        return None
    else:
        s = s.strip().replace("><", " ")
        list_elements = s.split(" ")
        for i in list_elements:
            if "src=" in i:
                element = i[4:]
                element = element.replace('"', '')
                # print(element)
                matches = re.search(r"^https?://(?:www\.)?youtube\.com/embed/(.+)$", element, re.IGNORECASE)
                return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()