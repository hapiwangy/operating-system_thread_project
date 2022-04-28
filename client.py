import socket, threading, pickle, time
from tkinter import *
from tkinter import messagebox
PORT = 5050
FORMAT = "utf-8-sig"
Dis_msg = "disconnecting"
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "123.241.254.143"
ADDR = (SERVER, PORT)

datalock = threading.Lock()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_email():
    info = []
    sub = info1.get("1.0","end")
    fro = info2.get("1.0","end")
    to = info3.get("1.0","end")
    app_pass = info4.get("1.0","end")
    content = info5.get("1.0","end")
    print(sub, fro, to, app_pass, content)
    info.append(sub)
    info.append(fro)
    info.append(to)
    pac = (info, content,app_pass)
    sd = pickle.dumps(pac)
    client.send(sd)

def send(name, send_msg):
    msg = name + ":" +send_msg
    client.send(msg.encode(FORMAT))


def recive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            change_view(message)
            if message[-4:] == "exit":
                break
        except:
            print(f"error occur")
            client.close()
            break

def running():
    client.connect(ADDR)
    send(name,"")
    re_thread = threading.Thread(target=recive, daemon=True)
    re_thread.start()
    # send(name,"")
    # while True:
    #     time.sleep(0.1)
    #     send_msg = input(f"{name}:")
    #     if send_msg == "send_email":
    #         send(name, "iwse")
    #         time.sleep(1)
    #         thread = threading.Thread(target = send_email)
    #         thread.start()
    #         thread.join()
    #     elif send_msg == "exit":
    #         send(name, "bye bye")
    #         break
    #     else:
    #         send(name, send_msg)
    #         change_view(name+":"+send_msg)
def change_view(message):
    text.insert(END, message+"\n")

def send_msg():
    message = text1.get("1.0","end").strip()
    if message == "exit":
        send(name, "bye bye")
        text1.delete("1.0","end")
    elif message != "":
        send(name, message)
        text1.delete("1.0","end")
    else:
        messagebox.showinfo("inform", "message can not be emtpy")


if __name__ == "__main__":
    name = input("urname")
    thread = threading.Thread(target = running)
    thread.start()      
    window = Tk()
    window.title("client")
    window.geometry("580x320")
    window.resizable(False, False)
    text = Text(window, width = 60, height = 20)
    text.grid(row= 0 , column = 0)
    text1 = Text(window, width = 60, height = 3)
    text1.grid(row = 1, column = 0)
    frame1 = Frame(window)
    frame1.grid(row = 1, column=1)
    sbtn = Button(frame1, width=10, height=2,text = "send mes", command = send_msg).grid(column=0, row = 0)
    ebtn = Button(frame1, width=10, height = 2, text = "send email", command = send_email).grid(column = 1, row = 0)
    frame = Frame(window)
    frame.grid(row = 0, column = 1)
    li1 = Label(frame, text = "標題")
    li1.pack(side = "top")
    info1 = Text(frame, width = 20, height = 1,bg = "yellow")
    info1.pack(side = "top")
    li2 = Label(frame, text = "from")
    li2.pack(side = "top")
    info2 = Text(frame, width = 20, height = 1,bg = "red")
    info2.pack(side = "top")
    li3 = Label(frame, text = "to")
    li3.pack(side = "top")
    info3 = Text(frame, width = 20, height = 1,bg = "lightblue")
    info3.pack(side = "top")
    li4 = Label(frame, text = "mail_app_pass")
    li4.pack(side = "top")
    info4 = Text(frame, width = 20, height = 1,bg = "pink")
    info4.pack(side = "top")
    li5 = Label(frame, text = "內文")
    li5.pack(side = "top")
    info5 = Text(frame, width = 20, height = 1,bg = "gray")
    info5.pack(side = "top")
    x = StringVar()
    window.mainloop()