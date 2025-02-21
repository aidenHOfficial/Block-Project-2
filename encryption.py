def encrypt(text, shift):
    result = ""
    
    for char in text:
        char_shift = shift % 26

        new_char = chr(((ord(char.lower()) - ord('a') + char_shift) % 26) + ord('a'))
        
        if (char.isupper()):
            result += new_char.upper()

        else:
            result += new_char
    
    return result

text = input("Enter some text to encrypt: ")
shift = 3
encrypted_text = encrypt(text, shift)
print(f"Your encrypted message: {encrypted_text}")
