# print("\n-----Practice Set 1-----")
# f = open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt")
# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

# from asyncore import read, write
# print("\n-----Practice Set 2-----")
# def game():
#     return 446
# score = game()
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\highscore.txt", "r") as f:
#     highscore = f.read()
# if highscore=="":
#     with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\highscore.txt", "w") as f:
#         f.write(str(score))
# elif int(highscore) < score:
#     with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\highscore.txt", "w") as f:
#         f.write(str(score))

# print("\n-----Practice Set 3-----")
# for i in range(2, 21):
#     with open(f"C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\Tables\\Multiplication_of_{i}.txt", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{i} * {j} = {i*j}\n")
#     # break

# print("\n-----Practice Set 4-----")
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt") as f:
#     content = f.read()
# content = content.replace("donkey", "$#@%&^")
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt","w") as f:
#     f.write(content)

# print("\n-----Practice Set 5-----")
# list = ["donkey", "mote", "gadhe"]
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt") as f:
#     content = f.read()
# for i in list:
#     content = content.replace(i, "$#@%&^")
#     with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt","w") as f:
#         f.write(content)

# print("\n-----Practice Set 6-----")
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt") as f:
#     search = f.read()
# if "python" in search.lower():
#     print("Yes python is present")
# else:
#     print("No python is not there")

# print("\n-----Practice Set 7-----")
# content = True
# i = 1
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt") as f:
#     while content:
#         content = f.readline()
#         if "python" in content.lower():
#             print(content)
#             print(f"Python is present in line number {i}")
#         i = i + 1

# print("\n-----Practice Set 8-----")
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt") as f:
#     search1 = f.read()
# with open(f"C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems_copy.txt", "w") as f:
#     f.write(search1)

# print("\n-----Practice Set 9-----")
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems.txt") as f:
#     search1 = f.read()
# with open(f"C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems_copy.txt") as g:
#     search2 = g.read()
# if search1 == search2:
#     print("These files are identical")
# else:
#     print("These are not identical")

# print("\n-----Practice Set 9-----")
# with open("C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems1.txt") as f:
#     wait = f.read()
# rule = ""
# with open(f"C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\poems1.txt", "w") as f:
#     f.write(rule)

# import os
# oldfile = "C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\Rename.txt"
# newfile = "C:\\Personal_Storage\\Animation\\5. Scripting\\Python_Code_With_Harry\\File_I_O\\remaned_in_python.txt"
# with open(oldfile) as f:
#     content3 = f.read()
# with open(newfile, "w") as f:
#     f.write(content3)

# os.remove(oldfile)