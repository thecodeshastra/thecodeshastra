from audioop import avg


a = "Mahendra" # string
d = 'Pawar' # string
e = '''Let the show begin''' # string
f = """Let it be string""" # string
b = 345 # integer
c = 72.22 # floating point
g = True # or false These are boolean
h = None # none

print("All Variables")# printing the variables
print(a)
print(d)
print(e)
print(f)
print(b)
print(c)
print(g)
print(h)

print("\nType of variables")# printing the typeof variables
print(type(a))
print(type(d))
print(type(e))
print(type(f))
print(type(b))
print(type(c))
print(type(g))
print(type(h))

# Operators
print("\nArithmetic Operators")# Arithmetic operators 
a = 3
b = 4
print("The value of a is : ", a)
print("The value of b is : ", b)
print("The addition value of a and b is : ", a+b)
print("The substructive value of a and b is : ", a-b)
print("The multiply value of a and b is : ", a*b)
print("The divisive value of a and b is : ", a/b)
print("The modulelation value of a and b is : ", a%b) # the remainder

print("\nAssignment Operators")# Assignment operator
a = 30
print(a)
a += 5 # it will add 5 to a
print(a)
a -= 3 # it will substract 3 from a 
print(a)
a *= 10 # it will Multiply 10 to a 
print(a)
a /= 10 # it will divide 10 from a "Note if it is division it will come in floating point"
print(a)

print("\nComparision Operators")# Comparision operator "Returns bool value"
e = (4>7)
f = (14<42)
g = (14>=7)
h = (52<=72)
i = (72!=72)
j = (14==7)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)

print("\nLogical operators") #Logical operator "works on boolean values"
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is : ", (bool1 and bool2)) # both has to true to return true
print("The value of bool1 or bool2 is : ", (bool1 or bool2)) # any one has to true to return true
print("The value of not bool2 is : ", (not bool2)) # returns the opposite
print("The value of not bool1 is : ", (not bool1)) # returns the opposite

print("\nType Casting")# Type casting in python
# It is used to convert one data type to another
Aa = "3534"
print(type(Aa))
Aa = int(Aa)
print(Aa + 5)
print(type(Aa))

print("\nInput function") # Input function in python
z = int(input("Enter you name :- ")) # it will input only integer
print("Hello,", z)

#practice set
print("\n")
i = 34
o = 35
p = i+o
i = str(i)
o = str(o)
print("The sum of " + i + " and " + o + " =", p)

print("\n")
Usr1 = int(input("Enter a number as user 1 : "))
Usr2 = int(input("Enter a number as user 2 : "))
avg = (Usr1+Usr2)/2
print("The average of user 1 and user 2 is : ", avg)

print("\n")
User1 = int(input("Enter a number you need square of : "))
User2 = str(User1)
print("The square of " + User2 + " is : ", User1*User1)