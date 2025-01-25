import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n) == 1:
            return e
    raise ValueError("No suitable 'e' found.")

def modular_inverse(e, phi_n):
    t, new_t = 0, 1
    r, new_r = phi_n, e
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise ValueError("e is not invertible")
    if t < 0:
        t += phi_n
    return t

def rsa_encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(encrypted_message, d, n):
    return "".join([chr(pow(char, d, n)) for char in encrypted_message])

def main():
    print("RSA Encryption and Decryption")

    # Input prime numbers p and q
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))

    # Check if both p and q are prime
    if not (p > 1 and all(p % i != 0 for i in range(2, int(math.sqrt(p)) + 1))):
        print("p is not a prime number.")
        exit()
    if not (q > 1 and all(q % i != 0 for i in range(2, int(math.sqrt(q)) + 1))):
        print("q is not a prime number.")
        exit()

    # Calculate n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Find public key e
    e = find_e(phi_n)
    d = modular_inverse(e, phi_n)

    # Print public and private keys
    print(f"Public Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")

    # Input message
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    encrypted_message = rsa_encrypt(message, e, n)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the message
    decrypted_message = rsa_decrypt(encrypted_message, d, n)
    print("Decrypted Message:", decrypted_message)

main()
