"""
make sure server.py is running before passing a message as commandline \
argument after client.py.
for example, a user will pass a message in terminal as below:
    python client.py this message will be echoed back

Once you enter the message, it will be printed on server terminal as well as \
client terminal.
And subsequently the socket on client terminal will be closed.

"""

import socket
import time
import sys


def client():
    socket.getaddrinfo('127.0.0.1', 3000)
    infos = socket.getaddrinfo('127.0.0.1', 3000)
    len(infos)
    stream_info = [i for i in infos if i[1] == socket.SOCK_STREAM][0]
    socket.getaddrinfo('127.0.0.1', 3000)
    stream_info
    client = socket.socket(*stream_info[:3])
    client
    client.connect(stream_info[-1])
    buffer_size = 8
    now = time.strftime('%H:%M:%S %d/%m/%Y')
    print('Starting server on port 3000 at {}'.format(now))
    try:
        message = sys.argv[1:]
        message = ' '.join(message)
        message = message.encode('utf8')
        print('sending {}'.format(message))
        client.sendall(message + b'\r')

        amount_received = 0
        amount_expected = len(message)
        echo_message = b''

        while amount_received < amount_expected:
            data = client.recv(buffer_size)
            amount_received += len(data)
            echo_message += data
        now = time.strftime('%H:%M:%S %d/%m/%Y')
        print('[{}] Echoed: {}'.format(now, echo_message.decode('utf8')))

    finally:
        print('closing socket')
        client.close()


if __name__ == "__main__":
    client()
