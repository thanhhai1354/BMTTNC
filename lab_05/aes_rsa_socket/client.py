from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import socket
import threading
import hashlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_key = RSA.generate(2048)

sever_public_key = RSA.import_key(client_socket.recv(2048))
client_socket.send(client_key.publickey().export_key(format='PEM'))

encrypt_aes_key = client_socket.recv(2048)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypt_aes_key) 

def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

def receive_message():
    while True:
        try:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                print("Server disconnected.")
                break  # Server disconnected
            decrypted_msg = decrypt_message(aes_key, encrypted_message)
            print(f"\nReceived: {decrypted_msg}")  # Add newline before the message
        except (ConnectionResetError, ConnectionAbortedError):
            print("Connection to server lost.")
            break  # Handle abrupt server disconnection

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

while True:
    message = input("Enter message: ")
    encrypted = encrypt_message(aes_key, message)
    client_socket.send(encrypted)
    if message == "exit":
        break
    
client_socket.close()