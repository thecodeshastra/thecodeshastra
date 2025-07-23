from datetime import date
import datetime
import sys
import inflect

def convert(user):
    try:
        p = inflect.engine()
        convertDate = datetime.datetime.strptime(user, '%Y-%m-%d')
        ExtractDate = convertDate.date()
        todayDate = date.today()
        days = todayDate - ExtractDate
        F = str(days).split()
        I = int(F[0]) * 1440
        word = p.number_to_words(I, andword="")
        return word.capitalize()
    except ValueError:
        sys.exit("Invalid date")

def main():
    U = input("Date of Birth: ")
    A = convert(U)
    print(f"{A} minutes")

if __name__ == "__main__":
    main()