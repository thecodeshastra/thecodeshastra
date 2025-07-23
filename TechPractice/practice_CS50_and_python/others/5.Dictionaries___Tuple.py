print("---Dictionaries---")
myDict = {
    "Name": "Mahendra",
    "Age": 24,
    "Learning": "Python",
    "List": [0,1,2,5,6],
    "anotherDict": {"Name": "Harry"},
    1: 5
}

print(myDict["Name"])
print(myDict['Age'])
print(myDict["anotherDict"]["Name"])
myDict["List"] = [1,2,9,11]
print(myDict["List"])

print("\n---Dict methods---")
print(type(myDict)) # type of dictionary
print(myDict.keys()) # prints the keys of the dictionary, you can also convert into list print(list(myDict.keys())
print(myDict.values()) # prints the values of the dictionary
print(myDict.items()) # prints the (key, values) of all contents in dictionary
print(myDict)
updateMyDict = {
    "Friend1": "Pinky",
    "Friend2": "Vishal"
}
myDict.update(updateMyDict) # updates the dictionary by adding key value pairs from udpateMyDict
print(myDict)

print(myDict.get("Name")) # prints value of given key
print(myDict["Name"]) # prints value of given key

# The difference between .get() and [] syntax in dictionary
print(myDict.get("Name1")) # returns none as Name1 is not present in the dictionary
# print(myDict["Name1"]) # throws error as Name1 is not present in the dictionary

print("\n---Sets---")
mySet = {1,3,6,8,10}
print(type(mySet))
print(mySet)
#Empty set
# Below syntax will create empty dictionary not set
Eset = {}
print(type(Eset))
# Below syntax will create empty set
Eseta = set()
print(type(Eseta))

#Adding values to empty set
Eseta.add(5)
Eseta.add(4)
Eseta.add(3)
# Eseta.add({8,9}) # you cannot add list or dictionary in set, you can add tuple in set as it is also non editable
print(len(Eseta)) # prints length of set
Eseta.remove(3) # removes 3 from set
# Eseta.remove(15) # throws error as 15 is not in the set
Eseta.pop() # removes random value from set, or specific value
Eseta.clear() # Empty the set
Eseta.union({8,3}) # returns set with values of both the sets
Eseta.intersection({8,11}) # returns a set which contains only items in both sets

print("\n---Pratice set 1---")
# write a program to create a hindi dictionary with value in english translate provide user option to look it up
Dictionary = {
    "Chamach": "Spoon",
    "Pankha": "Fan",
    "Jhadu": "Groom",
    "Pani": "Water"
}
print(Dictionary.keys())
Usr1 = input("Enter a Hindi word from list: ")
print("Translation of "+ Usr1 + " in English is: ", Dictionary[Usr1])

print("\n---Pratice set 2---")
# Write a program to input eight no from user and display unique no once
User1 = int(input("Enter a number1: "))
User2 = int(input("Enter a number2: "))
User3 = int(input("Enter a number3: "))
User4 = int(input("Enter a number4: "))
User5 = int(input("Enter a number5: "))
User6 = int(input("Enter a number6: "))
User7 = int(input("Enter a number7: "))
User8 = int(input("Enter a number8: "))

SetA = {User1, User2, User3, User4, User5, User6, User7, User8}
print(SetA)

print("\n---Pratice set 3---")
# Create an empty dictionary allow 4 friends to enter their favourite language as values and use keys as their names , Assume names are unique
favList = {}
U1 = input("Enter Fav language of Mahendra: ")
U2 = input("Enter Fav language of Pinky: ")
U3 = input("Enter Fav language of Praveen: ")
U4 = input("Enter Fav language of Dimple: ")

favList["Mahendra"] = U1
favList["Pinky"] = U2
favList["Praveen"] = U3
favList["Dimple"] = U4

print(favList)