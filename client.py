import socket, threading, pickle, time

PORT = 5050
FORMAT = "utf-8-sig"
Dis_msg = "disconnecting"
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "123.241.254.143"
ADDR = (SERVER, PORT)
flag = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def send(name, send_msg):
    msg = name + ":" +send_msg
    client.send(msg.encode(FORMAT))


def recive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            print(message)
            if message == "now shutting all client down":
                send(name, "exit")
                break
            elif message == "exit":
                break
        except:
            print(f"error occur")
            client.close()
            break

if __name__ == "__main__":
    client.connect(ADDR)
    name = input("ur name:")

    re_thread = threading.Thread(target=recive, daemon=True)
    re_thread.start()
    while True:
        time.sleep(0.5)
        send_msg = input(f"{name}:")
        send(name, send_msg)
        if send_msg == "exit":
            send(name, "bye bye")
            break    