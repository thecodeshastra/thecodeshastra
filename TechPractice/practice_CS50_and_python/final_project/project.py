import sys
from datetime import date
import os
import pyfiglet

figlet = pyfiglet.Figlet()
figlet.setFont(font="digital")

class Register():
    def __init__(self, standard, year):
        self.STD = standard
        self.Ayear = year
    
    def create_class(self):
        while True:
            self.student = input("-----Enter Name or press 0 to exit-----\nEnter student name : ")
            if self.student == "0":
                break
                sys.exit()
            else:
                with open(f"./{self.Ayear}/Class_{self.STD}/Student.csv", "a") as file:
                    file.write(f"{self.student}\n")
            
    
    def take_attendence(self):
        self.todayDate = date.today()
        try:
            with open(f"./{self.Ayear}/Class_{self.STD}/Student.csv") as file:
                for i in file:
                    _ = i[:-3]
                    while True:
                        UserInp = input(f"{i} - ")
                        if UserInp.lower() in ["a", "p"]:
                            with open(f"./{self.Ayear}/Class_{self.STD}/{_}.csv", "a") as Nfile:
                                Nfile.write(f"{self.todayDate},{UserInp.upper()}\n")
                            break
                        else:
                            print(figlet.renderText("Error"))
                            print("-----Enter A/a or P/p-----")
            sys.exit()
        except FileNotFoundError:
            print(figlet.renderText("Error"))
            print("-----Student file not found----- \n-----Please create student file using option 7-----")

    def add_student(self):
        try:
            while True:
                self.student = input("-----Enter Name or press 0 to exit-----\nEnter student name : ")
                if self.student == "0":
                    break
                else:
                    with open(f"./{self.Ayear}/Class_{self.STD}/Student.csv", "a") as file:
                        file.write(f"{self.student}\n")
            sys.exit()
        except FileNotFoundError:
            print(figlet.renderText("Error"))
            print("-----Student file not found----- \n-----Please create student file using option 7-----")

    def remove_student(self):
        try:
            while True:
                self.student = input("-----Enter Name or press 0 to exit-----\nEnter student name : ")
                if self.student == "0":
                    break
                else:
                    with open(f"./{self.Ayear}/Class_{self.STD}/Student.csv", "r") as file:
                        with open(f"./{self.Ayear}/Class_{self.STD}/tempStudent.csv", "w") as Ofile:
                            for line in file:
                                if self.student not in line.strip("\n"):
                                    Ofile.write(line)
                    os.replace(f"./{self.Ayear}/Class_{self.STD}/tempStudent.csv", f"./{self.Ayear}/Class_{self.STD}/Student.csv")
            sys.exit()
        except FileNotFoundError:
            print(figlet.renderText("Error"))
            print("-----Student file not found----- \n-----Please create student file using option 7-----")


def check_standard():
    try:
        STD =int(input("Enter standard/class you want to enter in: "))
        if STD in range(1,13):
            return STD
        else:
            print(figlet.renderText("Error"))
            print("-----Please enter a valid standard/class betweem 1-12-----")
            sys.exit()
    except ValueError:
        print(figlet.renderText("Error"))
        print("-----Standard/Class is not a valid integer plz enter between 1-12-----")
        sys.exit()

def academic_year():
    today = date.today()
    s = str(today).split("-")  
    cy = int(s[0])
    if s[1] in ["01","02","03", "04", "05"]:
        cy = cy - 1
    ny = str(cy + 1)
    return f"Academic_year_{cy}-{ny[2:]}"


def main():
    print("-----Welcome to Digital School Attendence Register-----")
    year = academic_year()
    standard = check_standard()
    if os.path.exists(f"./{year}/Class_{standard}"):
        pass
    else:
        os.makedirs(f"./{year}/Class_{standard}")
    reg = Register(standard, year)
    
    while True:
        intro = """\nPlease select a valid option
        1. Take attendence of selected class
        7. Create student list
        8. add a student in selected class
        9. Remove a student in selected class
        0. Exit the program
        """
        print(intro)
        try:
            User = int(input("Enter your choice : "))
            if User == 1:
                reg.take_attendence()
            elif User == 7:
                if os.path.exists(f"./{year}/Class_{standard}/Student.csv"):
                    print(figlet.renderText("Correction"))
                    print("\n-----File already exists----- \n-----please use 8 or 9 option to add or remove student-----")
                else:
                    reg.create_class()
                    sys.exit()
            elif User == 8:
                reg.add_student()
            elif User == 9:
                reg.remove_student()
            elif User == 0:
                sys.exit(pyfiglet.figlet_format("Thanks for using Digital School Register", font="slant"))
            else:
                print("\n-----Please select a valid Input-----")
        except ValueError:
            print(figlet.renderText("Error"))
            print("\n-----Choice is not a string, please select again-----")
            continue 

if __name__ == "__main__":
    main()