class Library:
    def __int__(self, BookList):
        self.books = BookList
    
    def DisplayListOfBooks(self):
        print("===Available books in Central Library===")
        for book in self.books:
            print(" -" + book)

    def requestBook(self, bookName):
        if bookName in self.books:
            print(f"Book {bookName} has been sent to you, Please return within 7days")
            self.books.remove(bookName)
            return True
        else:
            print(f"Sorry {bookName} is either not available or not returned, please check after few days")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for using book from central library, Have a great day")

class Student:
    def BorrowBook(self):
        self.Request = input("Enter the name of book you want to request : ")
        return self.Request

    def ReturnBook(self):
        self.Return = input("Enter the name of book you want to donate or return : ")
        return self.Return

if __name__ == "__main__":
    AvailableBooks = Library["Python", "C++", "C", "Java", "Django", "HTML", "Java script"]
    S1 = Student()
    while True:
        Intro = """\n===== Welcome to Central Library =====
        1. List of books available
        2. Request a book
        3. Return a book
        4. Exit the Library"""
        print(Intro)
        User = int(input("Enter your choice : "))
        if User == 1:
            AvailableBooks.DisplayListOfBooks()
        elif User == 2:
            AvailableBooks.requestBook(Student.BorrowBook())
        elif User == 3:
            AvailableBooks.requestBook(Student.ReturnBook())
        elif User == 4:
            print("Thanks for chosing Central Library.")
            exit()
        else:
            print("Please enter a valid choice!")