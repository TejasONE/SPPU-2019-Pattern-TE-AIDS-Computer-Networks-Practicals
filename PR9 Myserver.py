import socket

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', 6666))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            print('message=', data.decode())
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

