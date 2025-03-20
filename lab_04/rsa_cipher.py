import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generatekeys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate-keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Keys generated successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error: Server returned status code {response.status_code}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plaintext.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_ciphertext.setText(data['encrypted_message'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption successful")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error: Server returned status code {response.status_code}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_ciphertext.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plaintext.setText(data['decrypted_message'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption successful")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error: Server returned status code {response.status_code}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_verify.setText(data['signature'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signing successful")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error: Server returned status code {response.status_code}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_sign.toPlainText(),
            "signature": self.ui.txt_verify.toPlainText()  
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data['verified']:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Verification failed")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(f"Error: Server returned status code {response.status_code}")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Error: {str(e)}")
            msg.exec_()

def suppress_qt_warnings():
    import os
    os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"

if __name__ == "__main__":
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
