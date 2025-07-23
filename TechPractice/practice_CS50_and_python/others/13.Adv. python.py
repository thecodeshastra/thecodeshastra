# print("\n-----Practice Set 2-----")
# Name = input("Enter your name: ")
# Marks = int(input("Enter your marks: "))
# No = int(input("Enter you mobile number: "))
# print("The name of student is {}, his marks are {} and phone number is {}".format(Name, Marks, No))
# print("The name of student is {2}, his marks are {0} and phone number is {1}".format(Marks, No, Name))

# print("\n-----Practice Set 3-----")
# User = int(input("Enter a number you want table of : "))
# L1 = [str(User*i) for i in range(1,11)]
# # print(L1)
# a = "\n".join(L1)
# print(a)

# print("\n-----Practice Set 4-----")
# module = lambda x: x%5==0
# L5 = [9,8,9,5,10,15,21,25,35,39,49]
# a = list(filter(module, L5))
# print(a)

# print("\n-----Practice Set 5-----")
from functools import reduce
L6=[1,2,3,4,5,6,7,8,9,10]
a = reduce(max, L6)
print(a)
