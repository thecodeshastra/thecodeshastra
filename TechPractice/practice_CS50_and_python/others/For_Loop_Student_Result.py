#This is Exercise 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print (a)
for word in a:
    if word < 5:
        print ("this No. is less than 5 : ", word)

#This is Exercise 3
students = ["Rohan", "Sunny", "Akash", "Mohit", "Priya", "Shubhi", "Mona"]
passing = 33
print ("These are students of 6th standard" + str(students))
for student in students:
    print ("Sutdent name is : ", student)
    while True:
        marks = int(input("Enter Maths marks : "))
        if marks > 100:
            print ("You are typing in valid marks")
        else:
            break        
    if marks < 33:
        print ("You are fail")
    elif marks > 33:
        print ("You are pass")