import socket, threading, pickle, time
from xml.etree.ElementTree import TreeBuilder

from numpy import rec
PORT = 5050
FORMAT = "utf-8-sig"
Dis_msg = "disconnecting"
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "123.241.254.143"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(name, send_msg):
    msg = name + ":" +send_msg
    client.send(msg.encode(FORMAT))


def recive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            print(message)
            if message == "EVERYBODYLOGOUT":
                client.close()
                break
        except:
            print(f"error occur")
            client.close()
            break

def using():
    while True:
        time.sleep(0.5)
        send_msg = input(f"{name}:")
        send(name, send_msg)
        if send_msg == "exit":
            client.close()
            break
    send(name, "bye bye")

if __name__ == "__main__":
    client.connect(ADDR)
    name = input("ur name:")
    us_thread = threading.Thread(target=using)
    us_thread.start()
    re_thread = threading.Thread(target=recive)
    re_thread.start()