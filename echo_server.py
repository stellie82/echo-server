# Stella Kim
# Assignment 2: TCP/IP and Sockets

import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)  # server address

    # Instantiate TCP socket with IPv4 addressing
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,
                         socket.IPPROTO_TCP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # Bind new sock to address and begin to listen for connections
    sock.bind(address)
    sock.listen(1)

    try:
        while True:
            print('waiting for a connection', file=log_buffer)

            # Create a new socket and retrieve address when client connects
            conn, addr = sock.accept()

            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                while True:
                    data = conn.recv(16)  # 16-byte chunks
                    print('received "{0}"'.format(data.decode('utf8')))

                    if data:
                        conn.sendall(data)
                        print('sent "{0}"'.format(data.decode('utf8')))
                    else:
                        print('no data received')
                        break
            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                conn.close()
                print('echo complete, client connection closed',
                      file=log_buffer)

    except KeyboardInterrupt:
        sock.close()
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
