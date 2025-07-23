# Strings in python examples
a = "mahendra's"
b = 'mahendra"s'
c = '''Mah"e
endra's'''
print(a, b, c)
print(type(a))
print(type(b))
print(type(c))

print("\n-----String Slicing-----")# String slicing
greeting = "Good morning, "
name = "Mahendra"
# print(type(name))
# concatenating two strings
c = greeting + name
print(c)
name = "Mahendra"
print(name[5])
# name[3] = "d" # we can't change like this it will through error
print(name[1:4])
print(name[:5]) # same as print(name[0:5])
print(name[1:]) # same as print(name[1:7])
print(name[-4:-1]) # same as print(name[4:7])
print(name[0::2]) # slicing with skip values

print("\n-----String Functions-----")# String Functions
story = "once upon a time there was king who lost his kingdom and wins back with courage and patience to bring peace"
print(len(story)) # counts the length of string
print(story.endswith("peace")) # returns boolean value if it match or not
print(story.count("a")) # Counts any character in string or any word to check the count
print(story.capitalize()) # capitalize the first word as per english standard
print(story.find("and")) # Used to find any word will return the first location of it if return -1 means not there
print(story.replace("and", "&")) # replace old word with new from whole string

print("\n-----Escape sequence-----") # Escape sequence characters
# \' - Single Quote
# \\ - Backslash
# \n - New line
# \r - Carriage return
# \t - Tab
# \b - Backspace
# \f - Form feed
# \ooo - Octal value
# \xhh - Hex value

print("\n---User input good afternon---")
UserName = input("Enter your name : ")
print("Good afternon, ", UserName)

print("\n---User entered letter---")
Name = input("\nEnter your name: ")
Date = input("\nEnter your date: ")
print("Dear, " + Name + "\n\tYou are selected\n\t" + Date)

letter = "\nDear Mahendra,\n\tThis is new python training\nThanks!"
print(letter)