def atbash(userInput):
    print("-" * 20)
    userInput = str(input("Enter word that you want to cypher (with no spaces or numbers) : ".upper()))
    if not userInput.isalpha():
        print("You had an incorrect character in your input!")
        return False
    upOrLow = str(input("do you want the code to be Uppercase or lowercase: (Upper/Lower)"))
    if upOrLow.lower() != "upper" and upOrLow.lower() != "lower":
        print("You had an incorrect character in your input!")
        return False
    for char in userInput:
        shiftedDenary = (25 - (ord(char.upper()) - 65)) + 65
        if upOrLow.lower() == "upper":
           print(chr(shiftedDenary), end = " ")
           continue
        print(chr(shiftedDenary).lower(), end = " ")
    print()
    print("-" * 20)


def rot13():
    print("-" * 20)
    userInput = str(input("Enter your text or word: "))
    for char in userInput:
        if char == " ":
            print(" ", end = "")
        if char.isupper():
           print(chr((ord(char) - ord('A') + 13) % 26 + ord('A')), end = "")
        if char.islower():
            print(chr((ord(char) - ord('a') + 13) % 26 + ord('a')), end = "")
        else:
            print(char, end = "")
    print()
    print("-" * 20)


def caeser():
    print("-" * 20)
    userInput = str(input("Enter your text or word: "))
    shift = int(input("Enter what size of shift you want: ")) % 26
    output = ""
    for char in userInput:
        if char.isupper():
           i = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
           output += i
           print(i, end = "")
        elif char.islower():
            i = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            output += i
            print(i, end = "")
        else:
            output += char
            print(char, end = "")
    print()
    print("-" * 20)
    return output


def affine():
    print("-" * 20)
    userInput = str(input("Input a word or sentance you want to encrypt: "))
    multKey = int(input("Choose a mulitplication key between these numbers (5, 7, 9, 11, 15, 17, 19, 21, 23, or 25):  "))
    shift = int(input("Enter what size of shift you want: ")) % 26
    def mod_inverse(mult_key, alphabet_size=26):
        for mod_inverseA in range(1, alphabet_size):
            if (mult_key * mod_inverseA) % alphabet_size == 1:
                print(f"{mod_inverseA} is the modular inverse of {mult_key}")
                return mod_inverseA
        raise ValueError(f"There is no modular inverse for {mult_key}")
    check = mod_inverse(multKey)
    for char in userInput.upper():
        if char.isalpha():
            print(chr(((multKey * (ord(char) - ord("A")) + shift) % 26) + ord("A")), end = "")
        else:
            print(char, end = "")
    print()
    print("-" * 20)


def rail_fence():
    userInput = str(input("Input a word or sentance you want to encrypt: "))
    num_rails = int(input("How many rails do you want: "))
    rail = 0
    direction = 1
    rail_texts = [''] * num_rails
    for char in userInput:
        rail_texts[rail] += char
        rail += direction
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    print(''.join(rail_texts))
    return ''.join(rail_texts)


