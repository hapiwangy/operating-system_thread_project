import socket, threading, pickle
# 功能可以接收訊息(基本)，之後要可以進型別的處理(爬蟲、寄信等等)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
Dis_msg = "disconnecting"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORAMT = "utf-8-sig"

def handle_msg(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected")
    connected = True
    while connected:
        data = b""
        msg = conn.recv(4096)
        data = pickle.loads(msg)
        if  data[1] == "exit":
            break
        else:
            print(f"{data[0]} says {data[1]}")
    conn.close()
    print(f"DISCONNECTED!!")
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_msg, args = (conn, addr))
        thread.start()
        print(f"the number of activing thread is {threading.activeCount() - 1}")
if __name__ == "__main__":
    print("server is started at ", SERVER)
    start()