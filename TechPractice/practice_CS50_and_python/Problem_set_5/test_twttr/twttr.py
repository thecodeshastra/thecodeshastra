def main():
    U = input("Input: ")
    V = U.strip()
    print(shorten(V))

def shorten(word):
    l = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    S = ""
    A = []
    for c in word:
        if c in l:
            continue
        else:
            A.append(c)
    return S.join(A)

if __name__ == "__main__":
    main()