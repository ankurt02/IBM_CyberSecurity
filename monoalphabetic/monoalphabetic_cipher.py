import string
import random

def generate_key():
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)
    key = dict(zip(alphabet, shuffled_alphabet))
    return key

def encrypt(plaintext, key):
    ciphertext = ''.join(key.get(char, char) for char in plaintext.lower())
    return ciphertext

def decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    plaintext = ''.join(reverse_key.get(char, char) for char in ciphertext)
    return plaintext
