import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_MainWindow
import requests
import os
os.environ["QT_LOGGING_RULES"] = "qt.qpa.fonts=false"  # Suppress font warnings

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)
        if hasattr(self.ui, 'btn_genkeys'):
            self.ui.btn_genkeys.clicked.connect(self.call_api_gen_keys)

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate-keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Keys Generation Result")
                msg.setText("Keys have been generated successfully")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Error")
                msg.setText("Error while generating keys")
                msg.exec_()
        except requests.exceptions.RequestException as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText(f"Connection error: {str(e)}")
            msg.exec_()

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_signature.setText(data['signature'])

                msg = QMessageBox()
                msg.setWindowTitle("Sign Result")
                msg.setText("Sign Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_signature.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data['verified']:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information) 
                    msg.setText("Verify Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)  
                    msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

if __name__ == '__main__':
    os.environ["QT_QPA_PLATFORM"] = "windows:fontengine=freetype"  # Use freetype font engine
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())