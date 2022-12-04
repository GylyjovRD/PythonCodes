"""
CEASER CIPHER:
The Caesar cipher is named after Julius Caesar, who, according to Suetonius, 
used it with a shift of three (A becoming D when encrypting, and D becoming A when decrypting) 
to protect messages of military significance. While Caesar's was the first recorded 
use of this scheme, other substitution ciphers are known to have been used earlier.

This simple "mono-alphabetic substitution cipher" provides almost no security, 
because an attacker who has the encoded message can either use frequency analysis 
to guess the key, or just try all 25 keys.
"""

text = input("Enter the text you want to cypher: ")
k = int(input("Enter the key(needs to be integer): "))
language = input("Choose the language of the selected text(r)ussian or (e)nglish): ")

def ceaser_cipher(user, key, lang):
    res, n = [], ""

    # Check the selected langage and create the dictionary with the list of chars.
    if lang.lower() in ["р", "r"]:
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif lang.lower() in ["а", "e"]:
        dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        # return "The language you choose does not exist in options."
        dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    
    # Checking the symbol in text in each etaration
    for i in range(len(user)):

        # Check if the symbol upper or lower
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])
        
        if user[i] in n:
            for j in range(len(n)):
                # If the symbol number + key is in range of dictionary length
                # and if the symbol in text is equal to symbol in dictionary
                if 0 <= j + key < len(n) and user[i] == n[j]:
                    res.append(n[j + key])

                # If the symbol number + key is bigger than dictionary length
                # and if the symbol in text is equal to symbol in dictionary
                elif j + key >= len(n) and user[i] == n[j]:
                    res.append(n[(1 - j - key) % (len(n) - 1)])

                # If the symbol number + key is smaller than 0
                # and if the symbol in text is equal to symbol in dictionary
                elif j + key < 0 and user[i] == n[j]:
                    res.append(n[(j + key) % len(n)])
    
    return ''.join(res)


print(ceaser_cipher(text, k, language))