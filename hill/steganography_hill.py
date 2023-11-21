from hill_cipher import decrypt, encrypt, generate_key_matrix
import cv2
import os

def hide_message(img, msg, key):
    size = len(key)
    key_matrix = generate_key_matrix(key, size)

    n, m, z = 0, 0, 0
    for i in range(0, len(msg), size):
        block = msg[i:i+size]
        encrypted_block = encrypt(block, key_matrix)
        
        for char in encrypted_block:
            img[n, m, z] = ord(char) - ord('a')
            n += 1
            m += 1
            z = (z + 1) % 3

    return img

def reveal_message(img, key, msg_length):
    size = len(key)
    key_matrix = generate_key_matrix(key, size)

    message = ""
    n, m, z = 0, 0, 0
    blocks = msg_length // size

    for _ in range(blocks):
        block = ""
        for _ in range(size):
            block += chr(img[n, m, z] + ord('a'))
            n += 1
            m += 1
            z = (z + 1) % 3

        decrypted_block = decrypt(block, key_matrix)
        message += decrypted_block

    return message

if __name__ == "__main__":
    img = cv2.imread("icecr.png")

    key = input("Enter the key for Hill cipher: ")
    msg = input("Enter your secret message: ")

    img = hide_message(img, msg, key)
    cv2.imwrite("stegofile_hill.png", img)
    os.system("stegofile_hill.png")

    # Decrypting
    key_to_reveal = input("Enter the key for Hill cipher: ")
    if key_to_reveal == key:
        revealed_msg = reveal_message(img, key, len(msg))
        print("Revealed message:", revealed_msg)
    else:
        print("Incorrect key")
