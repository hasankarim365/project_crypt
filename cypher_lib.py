import string

low_chars = string.ascii_lowercase
alphabet = list(low_chars)
ascii_lower = [ord(x) for x in alphabet]

def atbash():
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
    

