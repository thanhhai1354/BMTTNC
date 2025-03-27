import base64

def main():
    try:
        with open("data.txt", "r") as f:
            encoded_string = f.read().strip()
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")

        print(f"Chuỗi đã giải mã: {decoded_string}")

    except Exception as e:
        print(f"Lỗii: {str(e)}")

if __name__ == "__main__":
    main()