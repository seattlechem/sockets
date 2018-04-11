"""
This server will print the message passed in as commanline argument from \
client terminal and echo it back to client terminal. This server needs to \
be running before passing message from the client terminal. The server \
connection will stay open.
"""


import socket
import time


def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    PORT = 3000
    sock.bind(('127.0.0.1', PORT))
    sock.listen(10)
    now = time.strftime('%H:%M:%S %d/%m/%Y')
    print('Starting server on port {} at {}'.format(PORT, now))
    buffer_length = 8
    try:
        while True:
            current_connection, address = sock.accept()
            message = b''
            while True:
                    data = current_connection.recv(buffer_length)
                    message += data
                    if len(data) < buffer_length or b'\r' in data:
                        break
            now = time.strftime('%H:%M:%S %d/%m/%Y')
            print('[{}] Echoed: {}'.format(now, message.decode('utf8')))
            current_connection.sendall(message)
            current_connection.close()
    except KeyboardInterrupt:
        current_connection.close()
        sock.close()
        now = time.strftime('%H:%M:%S %d/%m/%Y')
        print('Stopping server on port {} at {}'.format(PORT, now))


if __name__ == "__main__":
    listen()
