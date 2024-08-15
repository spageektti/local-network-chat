import socket
import threading
import argparse

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Server: {message}")
        except:
            break

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    while True:
        message = input("You: ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Chat Client')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Server host to connect to')
    parser.add_argument('--port', type=int, default=12345, help='Server port to connect to')
    args = parser.parse_args()
    
    start_client(args.host, args.port)
