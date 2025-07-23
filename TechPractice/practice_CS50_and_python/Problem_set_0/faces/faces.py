def main():
    slight_smile = "🙂"
    Frowing_face = "🙁"
    IN = input("")
    words = IN.split(" ")
    for word in words:
        if word == ":)":
            print(slight_smile , end=" ")
        elif word == ":(":
            print(Frowing_face , end=" ")
        else:
            print(word , end=" ")
    print("")



main()