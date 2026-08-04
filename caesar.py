def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


text = input("Enter Message: ")
shift = int(input("Shift: "))

cipher = encrypt(text, shift)

print("Encrypted:", cipher)