alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caesar(message,number,todo):
    def encrypt(message,number):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        text_list = list(message)
        cipher = []
        items = len(text_list)
        for i in range (0,items):
            letter = text_list[i]
            if letter in alphabet:
                alpha = alphabet.index(letter)
                alpha = alpha + number
                if alpha >25:
                    alpha -= 26
                    word = alphabet[alpha]
                    cipher.append(word)
                else:
                    word = alphabet[alpha]
                    cipher.append(word)
        print(" ".join(cipher))

    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    def decrypt(message,number):
            text_list = list(message)
            cipher = []
            items = len(text_list)
            for i in range (0,items):
                letter = text_list[i]
                if letter in alphabet:
                    alpha = alphabet.index(letter)
                    alpha = alpha - number
                    if alpha == 0:
                        alpha += 26
                        word = alphabet[alpha]
                        cipher.append(word)
                    else:
                        word = alphabet[alpha]
                        cipher.append(word)
            print(" ".join(cipher))
    
    if direction == "encode":
        encrypt(message=text,number=shift)
    elif direction == "decode":
        decrypt(message=text,number=shift)

caesar(message=text,number=shift,todo=direction)
