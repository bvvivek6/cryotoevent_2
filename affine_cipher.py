import random
from math import gcd

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist.")


def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            char = char.upper()
            x = ord(char) - ord('A')  
            encrypted_char = (a * x + b) % 26
            encrypted_text += chr(encrypted_char + ord('A'))  
        else:
            encrypted_text += char  
    return encrypted_text


def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    decrypted_text = ""
    a_inverse = mod_inverse(a, 26) 
    for char in ciphertext:
        if char.isalpha():  
            char = char.upper()
            y = ord(char) - ord('A')  
            decrypted_char = (a_inverse * (y - b)) % 26
            decrypted_text += chr(decrypted_char + ord('A'))  
        else:
            decrypted_text += char  
    return decrypted_text


def generate_random_keys():
    a = random.choice([i for i in range(1, 26) if gcd(i, 26) == 1])  
    b = random.randint(0, 25)  
    return a, b

def main():
    plaintext = input("Enter the plaintext: ")
    a, b = generate_random_keys()

    print("Randomly generated keys: a = {a}, b = {b}")
    
    # Encrypt
    ciphertext = affine_encrypt(plaintext, a, b)
    print("Encrypted text:", ciphertext)
    
    # Decrypj
    decrypted_text = affine_decrypt(ciphertext, a, b)
    print("Decrypted text:", decrypted_text)

main()

    