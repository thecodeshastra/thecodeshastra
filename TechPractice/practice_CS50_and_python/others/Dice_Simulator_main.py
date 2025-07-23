import random

print("--------------This is Dice Simulator-------------")
x = "y"
while x == "y":
    A = random.randint(1, 6)
    # print(A)
    if A == 1:
        print("[----------]")
        print("[          ]")
        print("[     @    ]")
        print("[          ]")
        print("[----------]")
    elif A == 2:
        print("[----------]")
        print("[          ]")
        print("[  @    @  ]")
        print("[          ]")
        print("[----------]")
    elif A == 3:
        print("[----------]")
        print("[        @ ]")
        print("[    @     ]")
        print("[ @        ]")
        print("[----------]")
    elif A == 4:
        print("[----------]")
        print("[ @      @ ]")
        print("[          ]")
        print("[ @      @ ]")
        print("[----------]")
    elif A == 5:
        print("[----------]")
        print("[ @      @ ]")
        print("[    @     ]")
        print("[ @      @ ]")
        print("[----------]")
    else:
        print("[----------]")
        print("[ @      @ ]")
        print("[ @      @ ]")
        print("[ @      @ ]")
        print("[----------]")

    x = input("press y to roll dice again: ")
