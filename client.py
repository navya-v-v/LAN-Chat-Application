import socket
import threading
from datetime import datetime

PORT = 5000

server_ip = input("Enter server IP address: ")
name = input("Enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((server_ip, PORT))
    print("\nConnected to the chat server!")
    print("Type 'exit' to leave the chat.\n")

except ConnectionRefusedError:
    print("\nConnection refused.")
    print("Make sure the server is running.")
    exit()

except socket.timeout:
    print("\nConnection timed out.")
    exit()

except OSError:
    print("\nCould not connect to the server.")
    print("Check the server IP address.")
    exit()


def get_timestamp():
    """Return the current time."""
    return datetime.now().strftime("%H:%M:%S")


def receive_messages():
    """Receive messages from the server."""
    while True:
        try:
            message = client.recv(1024)

            if not message:
                print("\nServer disconnected.")
                break

            print(f"\n{message.decode()}")
            print("You: ", end="", flush=True)

        except:
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

    if message.strip() == "":
        continue

    timestamp = get_timestamp()

    full_message = f"[{timestamp}] {name}: {message}"

    try:
        client.send(full_message.encode())

    except:
        print("\nCould not send message.")
        break
