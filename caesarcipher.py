
def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

# Get user input
mode = input("Type 'e' to encrypt or 'd' to decrypt: ")
text = input("Enter your message: ")
shift = int(input("Enter shift number: "))

# Process and show result
if mode == 'e':
    print("Encrypted:", encrypt(text, shift))
elif mode == 'd':
    print("Decrypted:", decrypt(text, shift))
else:
    print("Invalid choice!")