def extended_gcd(a, b):
    if a == 0:
        return b, 0
    if b == 0:
        return a, 1, 0  
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
def main():
    while True:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        gcd, x, y = extended_gcd(a, b)

        print(f"gcd({a}, {b}) = {gcd}")
        print(f"Coefficients: x = {x}, y = {y}")

        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

main()
        
