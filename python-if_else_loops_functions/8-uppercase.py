def uppercase(str):
    for i in range(len(str)):
        letter = str[i]
        if 97 <= ord(letter) and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
