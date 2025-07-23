# print("-----if, elif, else syntax examples-----")
# a = 15
# # Below is ladder of if, elif and else statements

# if (a>17):
#     print("The value of a is greater then 17")
# elif (a>13): # we can write n no of elif
#     print("The value of a is greater than 13")
# elif (a>3):
#     print("The value of a is greater than 3")
# elif (a>7):
#     print("The value of a is greater than 7")
# else:
#     print("The value of a is not greater than 3 or 7 or 13 or 17")

# print("\n-----Quick Test 1-----")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("yes")
# else:
#     print("No")

# print("\n-----practice set 1-----")
# N1 = int(input("Enter number 1: "))
# N2 = int(input("Enter number 2: "))
# N3 = int(input("Enter number 3: "))
# N4 = int(input("Enter number 4: "))

# if (N1>N4):
#     f1 = N1
# else:
#     f1 = N4

# if (N2>N3):
#     f2 = N2
# else:
#     f2 = N3

# if f1 > f2:
#     print(str(f1) + " is greatest")
# else:
#     print(str(f2) + " is greatest")

# print("\n-----Practice set 2 -----")
# S1 = int(input("Enter marks of subject 1: "))
# S2 = int(input("Enter marks of subject 2: "))
# S3 = int(input("Enter marks of subject 3: "))

# Total = S1+S2+S3
# avg = Total/3
# one way of writing code
# if avg>=40 and S1>=33 and S2>=33 and S3>=33:
#     print("Congratulation! You passed the examination.")
# else:
#     print("Sorry you failed, better luck next time")

# # if S1<33 or S2<33 or S3<33:
# #     print("Sorry you failed because of less than 33 markes in one of subjects.")
# # elif avg<40:
# #     print("Sorry, you failed because of total percentage less than 40.")
# # else:
# #     print("Congratulation you have passed the examination.")

# print("\n-----Practice set 3-----")
# list = ["make a lot of money", "subscribe this", "buy now", "click this", "subscribe now"]
# UserText = input("Please enter your text : ")
# UT = UserText.lower()

# # for i in list:
# #     # print(i)
# #     if i in UT:
# #         print("ERROR : This is spam !!!!")
# #         break
# if list[0] in UT:
#     print("ERROR : This is spam !!!!")
# elif list[1] in UT:
#     print("ERROR : This is spam !!!!")
# elif list[2] in UT:
#     print("ERROR : This is spam !!!!")
# elif list[3] in UT:
#     print("ERROR : This is spam !!!!")
# elif list[4] in UT:
#     print("ERROR : This is spam !!!!")
# else:
#     print("This is not a spam")

# print("\n-----Practice set 4-----")
# Username = input("Enter your username: ")
# print("Username size" + " " + str(len(Username)))
# if len(Username) > 10:
#     print("Your username is greater than 10 words")
# else:
#     print("Your username is of correct size")

# print("\n-----Practice set 5-----")
# List = ["Mahendra", "Pinky", "Praveen", "Dimple", "Hanuman","Pushpa","Rajesh"]
# name = input("Enter your name: ")
# if name in List:
#     print("You name is found in list")
# else:
#     print("Your name is not found in list")

Marks = int(input("Enter you marks : "))
if Marks > 100:
    print("Enter marks from 1-100")
elif Marks < 100 and Marks > 90:
    print("Your grade is EX")
elif Marks < 90 and Marks > 80:
    print("Your grade is A")
elif Marks < 80 and Marks > 70:
    print("Your grade is B")
elif Marks < 70 and Marks > 60:
    print("Your grade is C")
elif Marks < 60 and Marks >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")

