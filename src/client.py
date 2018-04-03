import socket
import time
import sys


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
    print('sending {}'.format(message))
    client.sendall(message.encode('utf8') + b'\r')

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = client.recv(buffer_size)
        amount_received += len(data)
    now = time.strftime('%H:%M:%S %d/%m/%Y')
    print('[{}] Echoed: {}'.format(now, data.decode('utf8')))

finally:
    print('closing socket')
    client.close()
