from cryptography.fernet import Fernet


# Generate a secret key
key = Fernet.generate_key()

# Create cipher object
cipher = Fernet(key)

# Original message
message = b"Student Result: Rahul Sharma - PASS"

# Encrypt the message
encrypted = cipher.encrypt(message)

# Decrypt the message
decrypted = cipher.decrypt(encrypted)


print("Original :", message.decode())
print("Encrypted:", encrypted.decode())
print("Decrypted:", decrypted.decode())