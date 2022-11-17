from server_8000 import TcpServer
from client_8000 import TcpClient


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=8000)
    srv2 = TcpServer(host='127.0.0.1', port=8001)
    try:
        srv.run()
        srv2.run()
    except KeyboardInterrupt:
        srv.stop()
        srv2.stop()
    myclient = TcpClient(host='127.0.0.1', port=8000)
    myclient.run()
    myclient2 = TcpClient(host='127.0.0.1', port=8001)
    myclient2.run()
