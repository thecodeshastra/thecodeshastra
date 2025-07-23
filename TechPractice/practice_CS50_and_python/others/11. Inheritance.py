# print("\n-----Practice Set 1-----")
# class C2dvector:
#     def __init__(self, i,j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"2d vector icap and jcap is {self.icap} * {self.jcap}"

# class C3dvector(C2dvector):
#     def __init__(self, i,j,k):
#         super().__init__(i,j)
#         self.kcap = k
    
#     def __str__(self):
#         return f"3d vector icap and jcap and kcap is {self.icap} * {self.jcap} * {self.kcap}"

# A = C2dvector(2,3)
# B = C3dvector(2,3,4)
# print(A)
# print(B)

# print("\n-----Practice Set 2-----")
# class Animals:
#     pass
# class pets(Animals):
#     pass
# class Dog(pets):
#     @staticmethod
#     def bark():
#         print("Dog will bark here, Bow bow!!!")

# Sunny = Dog()
# Sunny.bark()

# print("\n-----Practice Set 3-----")
# class Employeee:
#     salary = 1000
#     increment = 1.5
#     @property
#     def SAI(self):
#         return self.salary*self.increment
    
#     @SAI.setter
#     def SAI(self, salAfIncr):
#         self.increment = salAfIncr/self.salary

# E = Employeee()
# print(E.SAI)
# print(E.increment)
# E.SAI = 2000
# print(E.increment)

# print("\n-----Practice Set 4-----")
# class Complex:
#     def __init__(self, a , b):
#         # print("This is collection of complex numbers")
#         self.vala = a
#         self.valb = b

#     def __add__(self, c):
#         return Complex(self.vala + c.vala, self.valb + c.valb)
#     def __sub__(self, d):
#         return Complex(self.vala - d.vala, self.valb - d.valb)
#     def __mul__(self, c):
#         mulvala = (self.vala * c.vala) - (self.valb * c.valb)
#         mulvalb = (self.vala * c.valb) + (self.valb * c.vala)
#         return complex(mulvala, mulvalb)
#     def __str__(self):
#         if self.valb<0:
#             return f"{self.vala} - {-self.valb}i"
#         else:
#             return f"{self.vala} + {self.valb}i"
# C1 = Complex(3, 2)
# C2 = Complex(1, 7)
# print(C1 + C2)
# print(C1 - C2)
# print(C1 * C2)

# print("\n-----Practice Set 5-----")
# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         str1 = "" 
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range(len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)
    
#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# V3 = v1+v2
# V4 = v1*v2
# print(V3)
# print(V4)

# print("\n-----Practice Set 6-----")
# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

# v1 = Vector([1, 3, 9])
# v2 = Vector([7, 8, 10])
# print(v1)
# print(v2)

# print("\n-----Practice Set 7-----")
# class Vector:
#     def __init__(self, vec):
#        self.vec = vec
    
#     def __str__(self):
#         str1 = "" 
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         if len(self.vec) == len(vec2):
#             for i in range(len(self.vec)):
#                 newList.append(self.vec[i] + vec2.vec[i])
#             return Vector(newList)
#         else:
#             print("The length of vector 1 and vector 2 is not same for addition")
#             return 
    
#     def __mul__(self, vec2):
#         sum = 0
#         if len(self.vec) == len(vec2):
#             for i in range(len(self.vec)):
#                 sum += self.vec[i] * vec2.vec[i]
#             return sum
#         else:
#             print("The length of vector 1 and vector 2 is not same for multiplication")
#             return 

#     def __len__(self):
#         return len(self.vec)

# v1 = Vector([1, 4, 6, 8])
# v2 = Vector([1, 6, 9])
# v3 = v1+v2
# v4 = v1*v2
# print(v3)
# print(v4)
# print(len(v1))
# print(len(v2))