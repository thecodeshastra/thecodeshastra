# print("\n-----Practice Set 1-----")
# def Rfile(filename):
#     try:
#         with open(f"C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\TextFile\\{filename}", "r") as f:
#             file = f.read()
#             print(file)
#     except FileNotFoundError:
#         print(f"Error 404 :- File {filename} not found!!!")

# Rfile("1.txt")
# Rfile("2.txt")
# Rfile("3.txt")

# print("\n-----Practice Set 2-----")
# list1 = [1,2,3,4,5,6,7,8,9,10]
# for index,item in enumerate(list1):
#     if index==2 or index==4 or index==6:
#         print(f"{index} - {item}")

# print("\n-----Practice Set 3-----")
# User = int(input("Enter a number: "))
# L1 = [User*i for i in range(1,11)]
# print(L1)

# print("\n-----Practice Set 4-----")
# def division(a,b):
#     try:
#         divide = a/b
#         return divide
#     except ZeroDivisionError:
#         print("Infinite")
# U1 = int(input("Enter number 1: "))
# U2 = int(input("Enter number 2: "))
# a = division(U1,U2)

# print("\n-----Practice Set 5-----")
# User = int(input("Enter a number: "))
# L1 = [User*i for i in range(1,11)]
# print(L1)
# with open(f"C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\TextFile\\tables.txt", "a") as f:
#     file = f.write(f"The table of {User} is {L1}\n")