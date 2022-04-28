import socket, threading, pickle, time

PORT = 5050
FORMAT = "utf-8-sig"
Dis_msg = "disconnecting"
SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "123.241.254.143"
ADDR = (SERVER, PORT)

datalock = threading.Lock()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_email():
    datalock.acquire()
    info = []
    sub = input("subject")
    fro = input("from")
    to = input("to")
    which = input("pic or text")
    app_pass = input("email_app_pass")
    content = input("you content")
    info.append(sub)
    info.append(fro)
    info.append(to)
    pac = (info, which, content,app_pass)
    sd = pickle.dumps(pac)
    client.send(sd)
    datalock.release()

def send(name, send_msg):
    msg = name + ":" +send_msg
    client.send(msg.encode(FORMAT))


def recive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            print(message)
            if message == "exit":
                break
        except:
            print(f"error occur")
            client.close()
            break

def running():
    client.connect(ADDR)
    name = input("ur name:")
    re_thread = threading.Thread(target=recive, daemon=True)
    re_thread.start()
    while True:
        time.sleep(0.5)
        send_msg = input(f"{name}:")
        if send_msg == "send_email":
            send(name, "iwse")
            time.sleep(1)
            thread = threading.Thread(target = send_email)
            thread.start()
            thread.join()
        elif send_msg == "exit":
            send(name, "bye bye")
            time.sleep(2)
            break
        else:
            send(name, send_msg)


if __name__ == "__main__":
    running()        