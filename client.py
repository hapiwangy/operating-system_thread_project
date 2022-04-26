import socket, threading, pickle
PORT = 5050
FORMAT = "utf-8-sig"
Dis_msg = "disconnecting"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(name, send_msg):
    msg = (name, send_msg)
    message = pickle.dumps(msg)
    client.send(message)
if __name__ == "__main__":
    client.connect(ADDR)
    name = input("ur name:")
    while True:
        send_msg = input("輸入想傳送的msg:")
        send(name, send_msg)
        if send_msg == "exit":
            break
    send(name, "bye bye")