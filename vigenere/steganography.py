# steganography.py

import cv2
import os
from vigenere_cipher import encrypt, decrypt,generate_key

def hide_message(img, msg, password):
    key = generate_key(password, len(msg))

    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = ord(encrypt(msg[i], key[i]))
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def reveal_message(img, password):
    key = generate_key(password, len(img))

    message = ""
    n, m, z = 0, 0, 0

    for i in range(len(key)):
        message += decrypt(chr(img[n, m, z]), key[i])
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

if __name__ == "__main__":
    img = cv2.imread("C:\\Users\\acer\\Desktop\\ibm cyber sec\\pexels-photo-63764.jpeg")

    password = input("Enter a password: ")
    msg = input("Enter your secret message: ")

    img = hide_message(img, msg, password)
    cv2.imwrite("stegofile.jpg", img)
    os.system("stegofile.jpg")

    # Decrypting
    password_to_reveal = input("Enter the password: ")
    if password_to_reveal == password:
        revealed_msg = reveal_message(img, password)
        print("Revealed message:", revealed_msg)
    else:
        print("Incorrect password")
