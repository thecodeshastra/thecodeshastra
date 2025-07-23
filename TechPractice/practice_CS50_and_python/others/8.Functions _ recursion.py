# print("-----Quick quiz-----")
# def greet(name):
#     print("Good morning, " + name)
# User = input("Enter your name: ")
# greet(User)

# print("\n-----Practice Set 1-----")
# def max(num1, num2, num3):
#     if num1>num2:
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if num2>num3:
#             return num2
#         else:
#             return num3

# m = max(5,9,10)
# print(m)

# print("\n-----Practice Set 2-----")
# def Funct1(celcius):
#     far = (celcius * 1.8) + 32
#     return far
# a = int(input("Enter celcius value : "))
# C = Funct1(a)
# # C = int(Funct1(a))
# # print(C)
# print(f"The celcius to fahrenheit of {a} is {C}")

# print("\n-----Practice Set 3-----")
# # we can use end="" someting so that it will chnage the end of line work
# # as print is in built function we can edit the end
# print("Hello", end=" ")
# print(", How are you?")

# print("\n-----Practice Set 4-----")
# def funct2(n):
#     if n == 0:
#         return 0
#     else:
#         return n + funct2(n-1)
# input = int(input("Enter a number for sum of natural number : "))
# # input = 5
# a = funct2(input)
# print(a)

# print("\n-----Practice Set 5-----")
# def line(n):
#     for i in reversed(range(n)):
#         print("*" * (n-i))
#         if i == 0:
#             break
#         i = i - 1

# input1 = int(input("Enter a number : "))
# g = line(input1)
# print(g)

# print("\n-----Practice Set 6-----")
# def incm(value):
#     return value*2.54
# input2 = int(input("Enter inches : "))
# val = incm(input2)
# print(f"The centimeter value of inch {input2} is {val}")

# print("\n-----Practice Set 7-----")
# def strip_and_remove(string, word):
#     strNew = string.replace(word, "")
#     return strNew.strip()

# List = "     Mahendra is going to learn pythong           "
# a1 = strip_and_remove(List, "Mahendra")
# print(a1)

# print("\n-----Practice Set 8-----")
# def table(num):
#     i = 1
#     while i<11:
#         print(f"{num} * {i} = {num*i}")
#         i += 1
# User1 = int(input("Enter a no for table : "))
# a2 = table(User1)
# print(a2)