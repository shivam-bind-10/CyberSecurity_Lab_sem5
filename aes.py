
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes


def derive_key(password):
    digest = hashes.Hash(hashes.SHA256())
    digest.update(password.encode("utf-8"))
    return digest.finalize()


def encrypt_text(plaintext, password):
    key = derive_key(password)
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(
        nonce,
        plaintext.encode("utf-8"),
        None
    )

    return nonce.hex() + ":" + ciphertext.hex()


def decrypt_text(token, password):
    nonce_hex, ciphertext_hex = token.split(":", 1)

    key = derive_key(password)
    aesgcm = AESGCM(key)

    plaintext = aesgcm.decrypt(
        bytes.fromhex(nonce_hex),
        bytes.fromhex(ciphertext_hex),
        None
    )

    return plaintext.decode("utf-8")


if __name__ == "__main__":
    message = input("Enter text: ")
    password = input("Enter key: ")

    encrypted = encrypt_text(message, password)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt_text(encrypted, password))

