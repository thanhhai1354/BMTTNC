import socket
import ssl
import threading

server_address = ('localhost', 12345)

def recive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print(f"Nhận : {data.decode('utf-8')}")
    except:
        pass
    finally:
        ssl_socket.close()
        print("Kết nối đã ngắt")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)  
context.verify_mode = ssl.CERT_NONE
context.check_hostname = False  

ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')

ssl_socket.connect(server_address)

recive_thread = threading.Thread(target=recive_data, args=(ssl_socket,))
recive_thread.start()

try:
    while True:
        message = input("Nhập tin nhắn: ")
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    ssl_socket.close()