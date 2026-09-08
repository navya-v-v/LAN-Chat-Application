import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                if client in clients:
                    clients.remove(client)


def handle_client(client, address):
    print(f"[CONNECTED] {address}")

    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print(f"{address}: {message.decode()}")

            broadcast(message, client)

        except:
            break

    if client in clients:
        clients.remove(client)

    client.close()

    print(f"[DISCONNECTED] {address}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("=================================")
print("        LAN CHAT SERVER")
print("=================================")
print(f"Server is running on port {PORT}")
print("Waiting for clients...\n")


while True:
    client, address = server.accept()

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()
