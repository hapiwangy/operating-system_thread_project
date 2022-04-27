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
        if x == conn:
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
        if  data[-4:] == "exit":
            conn.send("exit".encode(FORMAT))
            connected = False
            conn.close()
            kickout(conn)
            break
        else:
            broadcast(data)
            print(f"{data}")
    print(f"DISCONNECTED!!")
def control():
    while True:
        message = input("輸入指令")
        if message == "shutdownclient" and len(peoples_in_room) != 0:
            broadcast("now shutting all client down")
            time.sleep(2)
            print(f"server and clients shutdown")
        elif len(peoples_in_room) == 0:
            print("現在沒人")
        elif message == "listall":
            for people in peoples_in_room:
                print(f"{people}")
        elif message == "shutdownserver":
            server.close()
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = announce, args = (conn, ))
        thread.start()
        thread1 = threading.Thread(target = handle_msg, args = (conn, addr))
        thread1.start()
        print(f"now we got {threading.activeCount() - 3} in our chatting room.")
if __name__ == "__main__":
    print("server is started at ", SERVER)
    thread_s = threading.Thread(target=start)
    thread_s.start()
    thread_c = threading.Thread(target=control)
    thread_c.start()
    