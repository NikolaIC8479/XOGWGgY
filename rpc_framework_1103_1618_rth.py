# 代码生成时间: 2025-11-03 16:18:15
import json
import socket
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal
from PyQt5.QtNetwork import QTcpServer, QTcpSocket

"""
这是一个简单的基于Python和PyQt框架的RPC远程调用框架。
该框架允许客户端和服务器之间进行远程过程调用。
"""

class RPCServer(QTcpServer):
    def __init__(self):
        super().__init__()

        # 初始化信号
        self.request_received = pyqtSignal(bytes)
        self.response_sent = pyqtSignal()

    def incomingConnection(self, socketDescriptor):
        """
        当有新连接时，创建一个新的QTcpSocket对象
        """
        client_socket = QTcpSocket(self)
        client_socket.setSocketDescriptor(socketDescriptor)
        client_socket.readyRead.connect(self.process_request)
        client_socket.bytesWritten.connect(self.response_sent)

    def process_request(self):
        """
        处理客户端发送的请求
        """
        client_socket = self.sender()
        request = client_socket.readAll()
        self.request_received.emit(request)

    def handle_request(self, request: bytes):
        """
        处理请求并返回响应
        """
        try:
            # 解析请求
            data = json.loads(request)
            # 调用对应的函数
            if data['method'] == 'add':
                result = self.add(data['params'][0], data['params'][1])
            elif data['method'] == 'subtract':
                result = self.subtract(data['params'][0], data['params'][1])
            else:
                raise ValueError('Unknown method')

            # 生成响应
            response = {'id': data['id'], 'result': result}
            self.send_response(response)
        except (json.JSONDecodeError, ValueError) as e:
            self.send_error_response(str(e))

    def add(self, a, b):
        """
        加法函数
        """
        return a + b

    def subtract(self, a, b):
        """
        减法函数
        """
        return a - b

    def send_response(self, response):
        """
        发送响应到客户端
        """
        client_socket = self.sender()
        response_bytes = json.dumps(response).encode('utf-8')
        client_socket.write(response_bytes)

    def send_error_response(self, error_message):
        """
        发送错误响应到客户端
        """
        client_socket = self.sender()
        error_response = {'id': None, 'result': None, 'error': error_message}
        error_response_bytes = json.dumps(error_response).encode('utf-8')
        client_socket.write(error_response_bytes)

class RPCClient(QWidget):
    def __init__(self, server_ip, server_port):
        super().__init__()

        self.server_ip = server_ip
        self.server_port = server_port
        self.tcp_socket = QTcpSocket()
        self.tcp_socket.connected.connect(self.on_connected)
        self.tcp_socket.readyRead.connect(self.process_response)
        self.tcp_socket.errorOccurred.connect(self.handle_error)
        self.tcp_socket.connectToHost(self.server_ip, self.server_port)

    def on_connected(self):
        """
        当客户端连接到服务器时
        """
        print('Connected to server')

    def process_response(self):
        """
        处理服务器的响应
        """
        response = self.tcp_socket.readAll()
        print('Response from server:', response)

    def handle_error(self, error):
        """
        处理连接错误
        """
        print('Error:', error)

    def send_request(self, method, params, id):
        """
        发送请求到服务器
        """
        request = {'id': id, 'method': method, 'params': params}
        request_bytes = json.dumps(request).encode('utf-8')
        self.tcp_socket.write(request_bytes)

if __name__ == '__main__':
    app = QApplication([])

    server = RPCServer()
    server.listen(QTcpServer.Address.Any, 12345)
    server.request_received.connect(server.handle_request)
    server.response_sent.connect(server.request_received.disconnect)

    client = RPCClient('localhost', 12345)
    client.send_request('add', [5, 3], 1)
    client.send_request('subtract', [10, 6], 2)

    app.exec_()