name = input("Enter your name : ")
marks = int(input("Enter your marks : "))
print ("Your name is" + " " + name)
print ("Your marks is" + " " + str(marks))

if marks > 100:
    print ("You are typing in valid marks")
elif marks > 75:
    print ("You scored First class with distinction")
elif marks in range(61, 75):
    print ("You scored First class")
elif marks in range(51, 60):
    print ("You scored Second class")
elif marks in range(34, 50):
    print ("You scored Third class")
elif marks < 33:
    print ("Sorry! You Failed")