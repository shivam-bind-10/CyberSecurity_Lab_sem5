from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)


# Generate public key from private key
public_key = private_key.public_key()


# Original message
message = b"Student Result: PASS"


# Encrypt using public key
encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(
            algorithm=hashes.SHA256()
        ),
        algorithm=hashes.SHA256(),
        label=None
    )
)


# Decrypt using private key
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(
            algorithm=hashes.SHA256()
        ),
        algorithm=hashes.SHA256(),
        label=None
    )
)


print("Original :", message.decode())
print("Encrypted:", encrypted.hex())
print("Decrypted:", decrypted.decode())