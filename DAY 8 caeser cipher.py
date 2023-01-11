alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar(message,number):
    text_list = list(message)
    cipher = []
    items = len(text_list)
    for i in range (0,items):
        letter = text_list[i]    
        if direction == "encode": 
            if letter in alphabet:
                    alpha = alphabet.index(letter)
                    alpha = alpha + number
        elif direction == "decode":
            if letter in alphabet:
                    alpha = alphabet.index(letter)
                    alpha = alpha - number
        word = alphabet[alpha]
        cipher.append(word)
    print(" ".join(cipher))
                    

caesar(message=text,number=shift)
