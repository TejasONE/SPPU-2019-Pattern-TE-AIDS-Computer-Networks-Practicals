import socket

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 6666))
        message = "Hello Server"
        s.sendall(message.encode())
        s.close()
    except Exception as e:   # E capital
        print(e)

if __name__ == '__main__':
    main()

