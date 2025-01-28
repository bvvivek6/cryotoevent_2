import random

def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # No modular inverse if gcd(a, m) != 1
    else:
        return x % m

def elgamal_encrypt(plaintext_number, p, e1, e2):
    r = random.randint(1, p - 1)
    c1 = modular_exponentiation(e1, r, p)
    c2 = (plaintext_number * modular_exponentiation(e2, r, p)) % p
    return c1, c2

def elgamal_decrypt(c1, c2, d, p):
    s = modular_exponentiation(c1, d, p)
    s_inv = mod_inverse(s, p)
    if s_inv is None:
        raise ValueError("No modular inverse found!")
    plaintext_number = (c2 * s_inv) % p
    return plaintext_number

# Example usage
if __name__ == "__main__":
    # Get user input for public and private keys, and numeric plaintext
    p = int(input("Enter a large prime number (p): "))
    e1 = int(input("Enter the base (e1): "))
    d = int(input("Enter the private key (d): "))

    # Calculate e2 from e1 and d
    e2 = modular_exponentiation(e1, d, p)

    # Get numeric plaintext input (plaintext treated as a number)
    plaintext_number = int(input("Enter the numeric plaintext to encrypt: "))

    # Encrypt the plaintext
    c1, c2 = elgamal_encrypt(plaintext_number, p, e1, e2)
    print(f"Ciphertext: (c1={c1}, c2={c2})")

    # Decrypt the ciphertext
    decrypted_number = elgamal_decrypt(c1, c2, d, p)
    print(f"Decrypted: {decrypted_number}")
