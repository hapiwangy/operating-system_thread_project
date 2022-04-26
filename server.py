import socket, threading, pickle, time
# 功能可以接收訊息(基本)，之後要可以進型別的處理(爬蟲、寄信等等)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
Dis_msg = "disconnecting"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = "utf-8-sig"

peoples_in_room = []
def announce(conn,):
    peoples_in_room.append(conn)
def kickout(conn):
    for x in peoples_in_room:
        if x[0] == conn:
            peoples_in_room.remove(x)
            break
    print(peoples_in_room)

def broadcast(message):
    data = message.encode(FORMAT)
    for people in peoples_in_room:
        people.send(data)
   
def handle_msg(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected")
    connected = True
    while connected:
        data = conn.recv(1024).decode(FORMAT)
        broadcast(data)
        if  data[-4:-1] == "exit":
            kickout(conn)
            break
        else:
            print(f"{data}")
    conn.close()
    print(f"DISCONNECTED!!")

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = announce, args = (conn, ))
        thread.start()
        thread1 = threading.Thread(target=handle_msg, args = (conn, addr))
        thread1.start()

        print(f"now we got {threading.activeCount() - 1} in our chatting room.")
if __name__ == "__main__":
    print("server is started at ", SERVER)
    start()
    
    