<<<<<<< HEAD
import socket

HEADER = 64
PORT = 8000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DESCONECTADO "
SERVER = "192.168.0.107"       #"192.168.0.107"
# SERVER = "127.0.1.1" este server se usa para el caso de correr el codigo en linux
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("hola Jugador # 3 !")
input()
send("hola a todos !")
input()
send("hola grupo !")

=======
import socket

HEADER = 64
PORT = 8000
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DESCONECTADO "
SERVER = "192.168.0.107"       #"192.168.0.107"
# SERVER = "127.0.1.1" este server se usa para el caso de correr el codigo en linux
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("hola Jugador # 3 !")
input()
send("hola a todos !")
input()
send("hola grupo !")

>>>>>>> 061632cc20c5434b951d11dbeca10d2693ce7600
send(DISCONNECT_MESSAGE)