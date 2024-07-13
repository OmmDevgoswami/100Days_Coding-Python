alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = ''' 
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
██║     ██║██████╔╝███████║█████╗  ██████╔╝     
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''
print (logo)

def caesar_cipher(text, shift, direction = "encode"):
    cipher_text = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            cipher_text += alphabet[((alphabet.index(i))+shift)%26]
        else:
            cipher_text += i
    print(f"The {direction}d text is {cipher_text}")

x = 1
while (x == 1):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()    
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar_cipher(text, shift, direction )
    x = int(input("Type 1 to continue, type 0 to exit: "))
print ("Game Over !! Thanks for Playing.")