import socket, threading, pickle, time, sending
from winreg import HKEY_LOCAL_MACHINE

from tkinter import *
# 功能可以接收訊息(基本)，之後要可以進型別的處理(爬蟲、寄信等等)
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
Dis_msg = "disconnecting"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = "utf-8-sig"

peoples_in_room = []
nameandconn = []
record = ""


def announce(conn):
    peoples_in_room.append(conn)
def kickout(conn):
    for x in peoples_in_room:
        if x == conn:
            peoples_in_room.remove(x)
            break

def broadcast(message):
    data = message.encode(FORMAT)
    for people in peoples_in_room:
        people.send(data)
def do_email(conn):
    data = b""
    data = conn.recv(4096)
    data = pickle.loads(data)
    sending.send_mail(data[0], data[1], data[2], data[3])
def handle_msg(conn, addr):
    wtt(f"[NEW CONNECTIONS] {addr} connected")
    data = conn.recv(1024).decode(FORMAT)
    nameandconn.append((data[:-1], conn))
    wtt("welcome "+data[:-1])
    connected = True
    while connected:
        data = conn.recv(1024).decode(FORMAT)
        if data[-3:] == "bye":
            conn.send("exit".encode(FORMAT))
            kickout(conn)
            conn.close()
            break
        elif data[-4:] == "iwse":
            wtt(f"start doing {data}")
            thread = threading.Thread(target=do_email, args = (conn,))
            thread.start()
            thread.join()
        else:
            broadcast(data)
            wtt(data)
    wtt("DISCONNECTED")
def wtt(message):
    text.insert(END, message + "\n")
def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = announce, args = (conn, ))
        thread.start()
        thread1 = threading.Thread(target = handle_msg, args = (conn, addr))
        thread1.start()
        wtt(f"now we got {threading.activeCount() - 2} in our chatting room.")
def pcm():
    record = text.get("1.0","end")
    with open("chatting_record.txt","w+") as fp:
        fp.write(record)
        for x in nameandconn:
            fp.write(str(x)+"\n")
if __name__ == "__main__":
    window = Tk()
    window.title("Server_control")
    window.resizable(False, False)
    window.geometry("570x400")
    btn = Button(window, text = "print_chat_message",justify=CENTER, command = pcm).pack(side = "top")
    text = Text(window,height=2, width = 77)
    text.pack(side = "left",fill=Y)
    scrollbar = Scrollbar(window)
    scrollbar.config(command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side = "right", fill=Y)
    x = StringVar()
    wtt("server is started at " + str(SERVER))
    thread_s = threading.Thread(target=start)
    thread_s.start()
    window.mainloop()
    