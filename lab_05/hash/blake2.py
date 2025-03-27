import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    message = input("Enter a message: ")
    hashed_message = blake2(message.encode('utf-8'))
    print(f"Original message: {message}")
    print(f"Hashed message: {hashed_message.hex()}")

if __name__ == "__main__":
    main()