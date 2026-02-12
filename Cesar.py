def encrypt(word, key):
    result = ""

    for letter in word:
        if letter.isalpha():
            firstLetter = ord("A")
            new = (ord(letter) - firstLetter + key) % 26
            result += chr(firstLetter + new)
        else:
            result += letter

    return result


def decrypt(word, key):
    result = ""

    for letter in word:
        if letter.isalpha():
            firstLetter = ord("A")
            new = (ord(letter) - firstLetter - key) % 26
            result += chr(firstLetter + new)
        else:
            result += letter

    return result

def getKey():
    while True:
        try:
            return int(input("Please enter the key: "))
        except ValueError:
            print("Key must be a number -_-")


while True:
    
    answer = input("Encrypt(1) or Decrypt(2) or Exit(3)? ").lower()

    if answer == "encrypt" or answer == "1":
        word = input("Please enter the word that you wish to encrypt: ").upper()
        key = getKey()
        encryptedWord = encrypt(word, key)
        print("Result:", encryptedWord)

    elif answer == "decrypt" or answer == "2":
        word = input("Please enter the word that you wish to decrypt: ").upper()
        key = getKey()
        result = decrypt(word, key)
        print("Result:", result)

    elif answer == "exit" or answer == "3": 
        print("Bro we where having fun :(((( See you!")
        break
    
    else:
        print("Invalid option (r u dumb). Please choose 1, 2, or 3.")