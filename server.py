import socket
import threading
import argparse

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket, addr):
    print(f"Client {addr} connected.")
    clients.append(client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Client {addr}: {message}")
            broadcast(message, client_socket)  # Broadcast the message
        except:
            break

    print(f"Client {addr} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

def start_server(host='0.0.0.0', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Chat Server')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host to bind the server to')
    parser.add_argument('--port', type=int, default=12345, help='Port to bind the server to')
    args = parser.parse_args()
    
    start_server(args.host, args.port)
