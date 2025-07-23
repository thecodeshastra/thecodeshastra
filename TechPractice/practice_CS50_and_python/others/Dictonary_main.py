import json
from difflib import get_close_matches

data = json.load(open("data.json"))
# print(data["smoke"])

def translate(user):
    user.lower()
    if user in data:
        return data[user]
    elif user.title() in data:
        return data[user.title()]
    elif user.upper() in data:
        return data[user.upper()]
    elif len(get_close_matches(user, data.keys())) > 0:
        print("Did you mean %s instead" %get_close_matches(user, data.keys())[0])
        decision = input("Press Y for yes And press N for no :- ")
        if decision == "Y" or "y":
            return data[get_close_matches(user, data.keys())[0]]
        elif decision == "N" or "n":
            return ("Word Not Found.....")
        else:
            return ("You have written wrong word Please write Y or N instead")     
    else:
        print("Word Not Found.....")

user = input("Enter The Word To Search :- ")
output = translate(user)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
