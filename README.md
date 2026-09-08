# LAN-Based Client-Server Chat Application

A simple real-time chat application built using Python socket programming and multithreading.

This project allows multiple clients connected to the same Local Area Network (LAN) to communicate with each other through a central server.

## 📌 Project Overview

The LAN Chat Application follows a client-server architecture.

- The **server** accepts multiple client connections.
- Each client runs independently.
- The server receives messages from clients.
- The server broadcasts messages to all other connected clients.
- TCP sockets are used for reliable communication.
- Multithreading allows multiple clients to communicate at the same time.

## 🛠️ Technologies Used

- Python
- Socket Programming
- TCP/IP
- Multithreading
- Git & GitHub

## 📂 Project Structure

```text
LAN-Chat-Application/
│
├── client.py
├── server.py
├── requirements.txt
├── README.md
└── .gitignore
