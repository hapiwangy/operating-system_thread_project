import socket, threading
# 功能可以接收訊息(基本)，之後要可以進型別的處理(爬蟲、寄信等等)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
Dis_msg = "disconnecting"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORAMT = "utf-8-sig"

def handle_msg(conn, addr):
    pass
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