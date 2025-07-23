#List and Tuples
print("---List---")
# create a list using []
a = [1,26,25,24,23]
print(a) # you can print a list using print function

# Access element of list using index e.g.- a[0] a[1] a[2]
print(a[1])

# Change the value of list using 
a[1] = 28
print(a)

#We can create list using different types
c = [28, "Mah", 23.4, False, None]
print(c)

# List slicing
friends = ["Mahendra", "Pinky", "Vishal", "Keyur", "Madhura", "Keshvi", 45]
print(friends[0:4]) #slicing is done same as string
print(friends[0:6:2])

print("---List Methods---")# List Methods
L1 = [1,8,7,2,21,15]
print(L1)
# L1.sort() # Sorts the list in assending order
# L1.reverse() # invert the list from last to one
# L1.append(8) # adds 8 at the end of list
# L1.insert(2,8) # This will add 8 at index 2
# L1.pop(2) # delete index 2 value
# L1.remove(21) # Removes 21 from list
# print(L1)

print("---Tuples---")
# Create a tuple using ()
b = (1,26,25,24,23)

t1 = () # Empty tuple
t2 = (1) # wrong way to create tuple with single element
t3 = (1,) # Tuple with single element
print(t1, t2, t3)

# Printing the element of tuple using index
print(b[0])

# Cannot update the values of tuple
# It is biggest difference between list and tuple
# b[0] = 34 # it will give an error

t = (1,2,5,7,9,1,2,4,5,1,1,2,3)
print(t.count(1)) # count the 1's from tuple
print(t.index(1)) # finds the 1 at which index it is


print("\n---practice set 1---")#practice set 1
# Write a program to store seven fruits in a list entered by user
f1 = input("Enter Name of fruit 1: ")
f2 = input("Enter Name of fruit 2: ")
f3 = input("Enter Name of fruit 3: ")
f4 = input("Enter Name of fruit 4: ")
f5 = input("Enter Name of fruit 5: ")
f6 = input("Enter Name of fruit 6: ")
f7 = input("Enter Name of fruit 7: ")

fruits = [f1,f2,f3,f4,f5,f6,f7]
print("List of fruits are :- ", fruits)

print("\n---practice set 2---")
# Write a program to accept marks of 6 students and display them in sorted order
s1 = int(input("Enter no of student1: "))
s2 = int(input("Enter no of student2: "))
s3 = int(input("Enter no of student3: "))
s4 = int(input("Enter no of student4: "))
s5 = int(input("Enter no of student5: "))
s6 = int(input("Enter no of student6: "))
Marks = [s1,s2,s3,s4,s5,s6]
Marks.sort()
print("Marks of students - ",Marks)

print("\n---Practice set 3---")
# Write a program to sum a list of 4 numbers
a1 = [1,2,3,4]
print(a1[0] + a1[1] + a1[2] + a1[3])
print(sum(a1))

print("\n---Practice set 4---")
# write a program to count 0 from tuple
tu1 = (7,0,8,0,0,9)
print(tu1.count(0))
