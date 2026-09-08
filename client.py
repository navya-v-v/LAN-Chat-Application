import socket
import threading

SERVER_IP = input("Enter server IP address: ")
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
    print("\nConnected to the chat server!")
except:
    print("\nCould not connect to the server.")
    exit()

name = input("Enter your name: ")


def receive_messages():
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            print("\n" + message.decode())
            print("You: ", end="")

        except:
            print("\nDisconnected from server.")
            break


receive_thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

receive_thread.start()


while True:
    message = input("You: ")

    if message.lower() == "exit":
        client.close()
        print("You left the chat.")
        break

    full_message = f"{name}: {message}"

    try:
        client.send(full_message.encode())
    except:
        print("Message could not be sent.")
        break
