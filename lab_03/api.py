from flask import Flask, request, jsonify
from cipher.ceasar import CeasarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các đối tượng mã hóa
ceasar_cipher = CeasarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailfenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

# ------------------- Ceasar Cipher ------------------- #
@app.route("/api/ceasar/encrypt", methods=["POST"])
def ceasar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = ceasar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/ceasar/decrypt", methods=["POST"])
def ceasar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = ceasar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# ------------------- Vigenere Cipher ------------------- #
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']  # Key là chuỗi
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# ------------------- Railfence Cipher ------------------- #
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])  # Giả sử key là số hàng (integer)
    encrypted_text = railfence_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# ------------------- Playfair Cipher ------------------- #
@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']  # Key thường là chuỗi, dùng để tạo bảng mã
    encrypted_text = playfair_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = playfair_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Thêm endpoint mới trước if __name__ == "__main__":
@app.route("/api/playfair/matrix", methods=["POST"])
def playfair_matrix():
    data = request.json
    key = data['key']
    matrix = playfair_cipher.get_matrix(key)
    return jsonify({'matrix': matrix})

# ------------------- Transposition Cipher ------------------- #
@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])  # Key có thể là chuỗi biểu diễn thứ tự cột, tùy theo cài đặt của bạn
    encrypted_text = transposition_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = transposition_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
