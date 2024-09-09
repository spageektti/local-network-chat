# Local Network Chat
![https://cloud-4ddqblov8-hack-club-bot.vercel.app/0zrzut_ekranu_20240823_170955.png](https://cloud-4ddqblov8-hack-club-bot.vercel.app/0zrzut_ekranu_20240823_170955.png)
This project implements a simple local network chat application using Python's `socket` and `threading` libraries. It consists of a chat server (`server.py`) and a chat client (`client.py`). Clients can connect to the server and exchange messages with each other in real time.

## Features

- **Multi-client support**: The server can handle multiple clients simultaneously.
- **Broadcast messaging**: Messages from one client are broadcast to all connected clients.
- **Simple command-line interface**: Users can specify the server and client configuration via command-line arguments.

## Requirements

- Python 3.x

## Usage

### 1. Start the Server

Run the `server.py` script to start the chat server.

```bash
python server.py --host 0.0.0.0 --port 12345
```

- `--host`: The IP address to bind the server to. Default is `0.0.0.0` (binds to all available interfaces).
- `--port`: The port number to bind the server to. Default is `12345`.

### 2. Start the Client

Run the `client.py` script to connect to the chat server.

```bash
python client.py --host 127.0.0.1 --port 12345
```

- `--host`: The server's IP address to connect to. Default is `127.0.0.1`.
- `--port`: The server's port number to connect to. Default is `12345`.

### 3. Chat!

Once the client is connected, type your messages and press Enter to send them. Messages from other clients will appear in the console.

## Example

Start the server:

```bash
python server.py --host 192.168.1.100 --port 8888
```

Start the client:

```bash
python client.py --host 192.168.1.100 --port 8888
```

Chat between multiple clients connected to the same server:

```text
You: Hello, everyone!
Server: Hi, welcome to the chat!
```

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Disclaimer

This is a basic implementation intended for educational purposes. It may not be secure or suitable for use in a production environment. Use at your own risk.
