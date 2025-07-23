# print("\n-----Practice Set 1-----")
# class Programmer:
#     company = "micrsoft"
#     def data(self, name, salary, age, gender):
#         self.name = name
#         self.salary = salary
#         self.age = age
#         self.gender = gender
#     def getInfo(self):
#        print(f"The name is {self.name} and age is {self.age} and gender is {self.gender} and salary is {self.salary}")

# Mah = Programmer()
# Pinky = Programmer()
# Mah.data("Mahendra Pawar", 30000, 24, "M")
# Pinky.data("Pinky Pawar", 25000, 23, "F")
# Mah.getInfo()
# Pinky.getInfo()

# print("\n-----Practice Set 2-----")
# import math as m
# class Maths:
#     Title = "Maths formula's"
#     def data(self, number):
#         self.digit = number
#     # def getInfo(self):
#     #    print(f"The square of {self.digit} is {self.digit*self.digit}")
#     #    print(f"The cube of {self.digit} is {self.digit*self.digit*self.digit}")
#     #    print(f"The square root of {self.digit} is {m.sqrt(self.digit)}")
#     def square(self):
#         print(f"The square of {self.digit} is {self.digit*self.digit}")
#     def cube(self):
#         print(f"The cube of {self.digit} is {self.digit*self.digit*self.digit}")
#     def squareRoot(self):
#         print(f"The square root of {self.digit} is {m.sqrt(self.digit)}")
# Name = Maths()
# a = int(input("Enter a number: "))
# Name.data(a)
# # Name.getInfo()
# Name.square()
# Name.cube()
# Name.squareRoot()

# print("\n-----Practice Set 3-----")
# class Test:
#     a = "Mahendra"
# object=Test()
# object.a = "Pinky"
# print(Test.a)
# print(object.a)
# # this will not change the class attribute
# # Answer is NO

# print("\n-----Practice Set 4-----")
# import math as m
# class Maths:
#     Title = "Maths formula's"
#     def data(self, number):
#         self.digit = number
#     # def getInfo(self):
#     #    print(f"The square of {self.digit} is {self.digit*self.digit}")
#     #    print(f"The cube of {self.digit} is {self.digit*self.digit*self.digit}")
#     #    print(f"The square root of {self.digit} is {m.sqrt(self.digit)}")
#     @staticmethod
#     def greet():
#         print("Hello user")
#         print("Following is calculation of square, cube and square root")
#     def square(self):
#         print(f"The square of {self.digit} is {self.digit*self.digit}")
#     def cube(self):
#         print(f"The cube of {self.digit} is {self.digit*self.digit*self.digit}")
#     def squareRoot(self):
#         print(f"The square root of {self.digit} is {m.sqrt(self.digit)}")
# Name = Maths()
# a = int(input("Enter a number: "))
# Name.data(a)
# # Name.getInfo()
# Name.greet()
# Name.square()
# Name.cube()
# Name.squareRoot()

# print("\n-----Practice Set 5-----")
# class Trainticket:
#     def __init__(self, trainName, amount, NoOfseats):
#         self.name = trainName
#         self.fare = amount
#         self.seats = [int(x) for x in range(1, (NoOfseats+1))]
#         # self.seatNum = 1
#     def getStatus(self):
#         print("----- Train status -----")
#         print(f"The Train name is {self.name}")
#         print(f"No of seats available is {self.seats}")
#         print(f"Tain fare : {self.fare}")
#         print("-----Status End-----")

#     def bookTicket(self):
#         if len(self.seats)>0:
#            print(f"\nYour ticket is booked, your seaat no is {self.seats[-1]}\n")
#            self.seats = self.seats[:-1]
#         else:
#             print("Sorry!, No. seats available")

#     def cancleTicket(self, seatNum):
#        print(f"\nYour ticket of following seat number {seatNum} has been canclled")

# passenger1 = Trainticket("Karnavati express : 01234", 300, 2)
# passenger1.getStatus()
# A = input("Do you want to book ticket type Y for yes, N for None and C for Cancle: ")
# if A.lower() == "y":
#     passenger1.bookTicket()
#     passenger1.getStatus()
# elif A.lower() == "c":
#     B = int(input("Enter your seat number: "))
#     passenger1.cancleTicket(B)
#     passenger1.seats.append(B)
#     passenger1.getStatus()
# else:
#     print("Thank you for checking here")

# print("\n-----Practice Set 6-----")
# class sample:
#     def __init__(slf, name):
#         slf.name = name

# a = sample("Mahendra")
# print(a.name)