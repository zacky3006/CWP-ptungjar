word = input()
for i in range(len(word)):
    if word[i].isupper():
        print(f"{word[i].lower()}", end="")
    else:
        print(f"{word[i].upper()}", end="")