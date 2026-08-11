
try:
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes
except ImportError as exc:
    raise ImportError(
        "Missing dependency: install it with 'python -m pip install cryptography'."
    ) from exc


def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_text(plaintext, public_key):
    ciphertext = public_key.encrypt(
        plaintext.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return ciphertext


def decrypt_text(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plaintext.decode("utf-8")


if __name__ == "__main__":
    message = input("Enter text: ")

    private_key, public_key = generate_keys()

    encrypted = encrypt_text(message, public_key)
    decrypted = decrypt_text(encrypted, private_key)

    print("Encrypted (hex):", encrypted.hex())
    print("Decrypted:", decrypted)

