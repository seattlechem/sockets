import socket
import time


def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 3000))
    sock.listen(10)
    now = time.strftime('%H:%M:%S %d/%m/%Y')
    print('Starting server on port 3000 at {}'.format(now))
    buffer_length = 8
    while True:
        try:
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


if __name__ == "__main__":
    listen()
