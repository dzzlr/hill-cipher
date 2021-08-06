import numpy as np                              # Created by Fakhri Hassan Maulana (1202194336)
from sympy import Matrix                        # From class SI-43-02

def translate_plaintext_and_key(plaintext, key):
    # Translate Plain with ASCII Method
    plainMatrix = np.array([[0]*(int(len(plaintext)/3)) for i in range(3)])
    m = 0
    for i in range(3):
        for j in range(int(len(plaintext)/3)):
            plainMatrix[i][j] = ord(plaintext[m]) % 65
            m += 1

    # Translate Key with ASCII Method
    keyMatrix = np.array([[0]*(int(len(key)/3)) for i in range(3)])
    k = 0
    for i in range(3):
        for j in range(int(len(key)/3)):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return plainMatrix, keyMatrix

def encrypt_process(plainMatrix, keyMatrix):
    multiplyMatrix = keyMatrix.dot(plainMatrix)
    return multiplyMatrix

def decrypt_process(plainMatrix, keyMatrix):
    inverse_key = np.array(Matrix(keyMatrix).inv_mod(26))
    multiplyMatrix = inverse_key.dot(plainMatrix)
    return multiplyMatrix

def output_cipher(plaintext, multiplyMatrix):
    cipherMatrix = multiplyMatrix % 26
    cipherText = ''
    for i in range(3):
        for j in range(int(len(plaintext)/3)):
            cipherText += chr(cipherMatrix[i][j] + 65)
    return cipherText

if __name__ == "__main__":
    choice = input("\n==== HILL CIPHER PROGRAM ====\n1. Encryption\n2. Decryption\nEnter the choice: ")
    if choice == "1":
        print("-------- Encryption ---------")
        plaintext = input("Plaintext: ").replace(" ", "").upper()
        key = input("Key: ").replace(" ", "").upper()
        plainMatrix, keyMatrix = translate_plaintext_and_key(plaintext, key)
        output_encrypt = output_cipher(plaintext, encrypt_process(plainMatrix, keyMatrix))
        print("Output:", output_encrypt)
    elif choice == "2":
        print("-------- Decryption ---------")
        plaintext = input("Plaintext: ").replace(" ", "").upper()
        key = input("Key: ").replace(" ", "").upper()
        plainMatrix, keyMatrix = translate_plaintext_and_key(plaintext, key)
        output_decrypt = output_cipher(plaintext, decrypt_process(plainMatrix, keyMatrix))
        print("Output:", output_decrypt)
    else:
        print("Invalid Choice")