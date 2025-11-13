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

def baconian():
    print("-" * 20)
    substitution = {
        "A": "aaaaa", "B": "aaaab", "C": "aaaba", "D": "aaabb", 
        "E": "aabaa", "F": "aabab", "G": "aabba", "H": "aabbb",
        "I": "abaaa", "J": "abaaa", "K": "abaab", "L": "ababa",
        "M": "abbaa", "N": "abbaa", "O": "abbab", "P": "abbba",
        "Q": "abbbb", "R": "baaaa", "S": "baaab", "T": "baaba",
        "U": "baabb", "V": "baabb", "W": "babaa","X": "babab",
        "Y": "babba", "Z": "babbb"
        }
    userInput = str(input("ENTER WORD THAT YOU WANT TO CYPHER (WITH NO SPACES OR NUMBERS) : ")).upper()
    output = []
    if not userInput.isalpha():
        print("You had an incorrect character in your input!")
        return False
    for char in userInput:
        for key, value in substitution.items():
            if key == char:
                output.append(value + " ")
    output = "".join(output)
    print(output)
    print("-" * 20)
    return output
    

def polybius_square():
    set_polybius_square = {
    'A': 'AA', 'B': 'AB', 'C': 'AC', 'D': 'AD', 'E': 'AE',
    'F': 'BA', 'G': 'BB', 'H': 'BC', 'I': 'BD', 'J': 'BE',
    'K': 'CA', 'L': 'CB', 'M': 'CC', 'N': 'CD', 'O': 'CE',
    'P': 'DA', 'Q': 'DB', 'R': 'DC', 'S': 'DD', 'T': 'DE',
    'U': 'EA', 'V': 'EB', 'W': 'EC', 'X': 'ED', 'Y': 'EE',
    'Z': 'FA'
    }
    output = []
    userInput = str(input("Input a word or sentance you want to encrypt: ")).upper()
    for char in userInput:
        if char == " ": 
            output.append("  ") 
        elif char.isalpha():
            for key, value in set_polybius_square.items():
                if char == key:
                    output.append(value + " ")
                    break  
        else:
            output.append(char + " ")
    output = "".join(output)
    print(output)
    return output
            
polybius_square()
