import hashlib

def calculate_md5(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_string = input("Enter a string: ")
md5_hash = calculate_md5(input_string)

print("MD5 hash:", md5_hash)