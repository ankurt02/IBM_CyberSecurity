from caesar_cipher import decrypt, encrypt
import cv2
import os

def hide_message(img, msg, key):
    n, m, z = 0, 0, 0

    # Store the length of the message in the first pixel
    msg_length = len(msg)
    img[n, m, z] = msg_length

    # Hide the message in the remaining pixels
    for char in msg:
        img[n, m, z] = ord(encrypt(char, key))
        n += 1
        m += 1
        z = (z + 1) % 3

    return img

def reveal_message(img, key):
    message = ""
    n, m, z = 0, 0, 0

    # Read the length of the message from the first pixel
    msg_length = img[n, m, z]

    # Decrypt the message from the remaining pixels
    for _ in range(msg_length):
        char = chr(img[n, m, z])
        message += decrypt(char, key)
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

if __name__ == "__main__":
    img = cv2.imread("ceaser\\banana.png")

    key = 3
    msg = str(input("Enter your secret message: "))

    img = hide_message(img, msg, key)
    cv2.imwrite("stego2_caesar.png", img)
    os.system("stego2_caesar.png")

    # Decrypting
    img_reloaded = cv2.imread("stego2_caesar.png")

    revealed_msg = reveal_message(img_reloaded, key)
    print("Revealed message:", revealed_msg)
