# Stella Kim
# Assignment 2: TCP/IP and Sockets

import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)

    # Instantiate TCP socket with IPv4 addressing
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,
                         socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address),
          file=log_buffer)

    sock.connect(server_address)  # connect to server
    received_message = ''

    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        sock.sendall(msg.encode('utf-8'))
        received = 0
        expected = len(msg)

        while received_message < expected:
            chunk = sock.recv(16)  # 16-byte chunks
            received += len(chunk)
            received_message += chunk.decode('utf8')
            print('received "{0}"'.format(chunk.decode('utf8')),
                  file=log_buffer)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print('closing socket', file=log_buffer)
        sock.close()
        return received_message


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
