import numpy as np
import string

def generate_key_matrix(key, size):
    key_matrix = np.zeros((size, size), dtype=int)
    key = key.lower().replace(" ", "")

    index = 0
    for i in range(size):
        for j in range(size):
            key_matrix[i][j] = ord(key[index]) - ord('a')
            index += 1

    return key_matrix
def encrypt(plaintext, key_matrix):
    size = len(key_matrix)
    plaintext = plaintext.lower()
    
    # Pad the plaintext with 'x' to make its length a multiple of the key size
    while len(plaintext) % size != 0:
        plaintext += 'x'

    ciphertext = ""
    for i in range(0, len(plaintext), size):
        block = np.array([ord(char) - ord(' ') for char in plaintext[i:i+size]])
        encrypted_block = np.dot(key_matrix, block) % 27
        ciphertext += ''.join([chr(char + ord(' ')) for char in encrypted_block])

    return ciphertext

def decrypt(ciphertext, key_matrix):
    size = len(key_matrix)
    
    # Calculate the modular inverse of the determinant of the key matrix
    det = int(round(np.linalg.det(key_matrix)))
    det_inv = pow(det, -1, 27)

    # Calculate the adjugate of the key matrix
    key_matrix_inv = (det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)) % 27

    plaintext = ""
    for i in range(0, len(ciphertext), size):
        block = np.array([ord(char) - ord(' ') for char in ciphertext[i:i+size]])
        decrypted_block = np.dot(key_matrix_inv, block) % 27
        plaintext += ''.join([chr(char + ord(' ')) for char in decrypted_block])

    return plaintext
