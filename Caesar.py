def encrypt(text, shift):
    s = ""
    for char in text:
        ascii = ord(char)
        new_ascii = ascii + shift
        new_char = chr(new_ascii)
        s = s + new_char
    return s

def decrypt(cipher, shift):
    s = ""
    for char in cipher:
        ascii = ord(char)
        new_ascii = ascii - shift
        new_char = chr(new_ascii)
        s = s + new_char
    return s

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

cipher = encrypt(text, shift)
print("Encrypted text:", cipher)

plain = decrypt(cipher, shift)
print("Decrypted text:", plain)
