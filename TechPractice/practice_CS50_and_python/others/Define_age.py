print ('*****Age INFO*****')
print("""Age is < 20 = KID
Age is > 20 and < 40 = ADULT
Age is > 40 = OLD """)

name = input("Enter your name : ")
age = int(input("Enter your age : "))
print ("Your name is" + " " + name)
print ("Your age is" + " " + str(age))

if age < 20:
    print("You are KID")
elif age in range(20, 40):
    print("You are ADULT")
if age > 40:
    print("You are OLD")