import socket
import system


def listen():
    # create TCP/IP socket
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind the socket to the port
    connection.bind(('127.0.0.1', 3000))
    # calling listen() puts the socket into server mode accept() waits for \
    # incoming connection
    connection.listen(10)
    now = system.datetime.datetime.now()
    print('Starting server on port 3000 at {}'.format(now))
    while True:
        # wait for connection
        current_connection, address = connection.accept()
        '''
        accept() returns an open connection between the server and client, \
        along with the address of the client. The connection is actually a \
        different socket on another port (assigned by the kernel). Data is \
        read from the connection with recv() and transmitted with sendall().
         '''
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
