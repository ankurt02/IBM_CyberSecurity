from monoalphabetic_cipher import decrypt, encrypt, generate_key
import cv2
import os

def hide_message(img, msg, key):
    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def reveal_message(img, key):
    c = {i: chr(i) for i in range(255)}

    message = ""
    n, m, z = 0, 0, 0

    while True:
        pixel_value = img[n, m, z]
        char = c.get(pixel_value, None)

        if char is not None:
            message += char
        else:
            break

        n += 1
        m += 1
        z = (z + 1) % 3

    return decrypt(message, key)

if __name__ == "__main__":
    img = cv2.imread("monoalphabetic\\R.png")

    key = generate_key()
    msg = input("Enter your secret message: ")
    encrypted_msg = encrypt(msg, key)

    img = hide_message(img, encrypted_msg, key)
    cv2.imwrite("stegofile.png", img)
    os.system("stegofile.png")

    password = input("Enter a password: ")
    if password == "123":
        decrypted_msg = reveal_message(img, key)
        print("Decrypted message:", decrypted_msg)
    else:
        print("Incorrect password")
