import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    word = sys.argv[1]
    text = sys.argv[2]

    matche = re.findall(word, text)

    if len(matche) == 0:
        print("none")
    else:
        print(len(matche))