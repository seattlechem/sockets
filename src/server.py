import socket
import system


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('127.0.0.1', 3000))
    connection.listen(10)
    now = system.datetime.datetime.now()
    print('Starting server on port 3000 at {}'.format(now))
    while True:
        current_connection, address = connection.accept()
        while True:
            data = current_connection.recv(2048)

            if data == 'quit\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                print('Stopping server on port 3000 at {}'.format(now))
                break

            elif data == 'stop\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                print('Stopping server on port 3000 at {}'.format(now))
                exit()

            elif data:
                current_connection.send(data)
                print('{} Echoed: \'{}\''.format(now, data))


if __name__ == "__main__":
    try:
        listen()
    except KeyboardInterrupt:
        pass
