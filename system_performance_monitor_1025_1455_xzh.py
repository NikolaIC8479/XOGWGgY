# 代码生成时间: 2025-10-25 14:55:01
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer, pyqtSlot

"""
一个简单的系统性能监控工具，使用pyqt5和psutil库。
该工具可以显示CPU使用率、内存使用量、磁盘使用量和网络IO统计。
"""

class SystemPerformanceMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置窗口标题和大小
        self.setWindowTitle('系统性能监控工具')
        self.setGeometry(100, 100, 600, 400)

        # 创建一个widget作为主窗口的容器
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # 创建一个垂直布局
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # 添加显示CPU使用率的标签
        self.cpu_label = QLabel('CPU使用率: 0%')
        self.layout.addWidget(self.cpu_label)

        # 添加显示内存使用量的标签
        self.memory_label = QLabel('内存使用量: 0GB')
        self.layout.addWidget(self.memory_label)

        # 添加显示磁盘使用量的标签
        self.disk_label = QLabel('磁盘使用量: 0GB')
        self.layout.addWidget(self.disk_label)

        # 添加显示网络IO统计的标签
        self.network_label = QLabel('网络IO统计: 0B/s')
        self.layout.addWidget(self.network_label)

        # 初始化定时器，每隔1秒更新一次数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def update_data(self):
        try:
            # 获取CPU使用率
            cpu_usage = psutil.cpu_percent(interval=1)
            self.cpu_label.setText(f'CPU使用率: {cpu_usage}%')

            # 获取内存使用量
            memory = psutil.virtual_memory()
            self.memory_label.setText(f'内存使用量: {memory.used / (1024 ** 3):.2f}GB')

            # 获取磁盘使用量
            disk = psutil.disk_usage('/')
            self.disk_label.setText(f'磁盘使用量: {disk.used / (1024 ** 3):.2f}GB')

            # 获取网络IO统计
            net_io = psutil.net_io_counters()
            self.network_label.setText(f'网络IO统计: {net_io.bytes_sent + net_io.bytes_recv}B/s')

        except Exception as e:
            print(f'更新数据时发生错误: {e}')

if __name__ == '__main__':
    if sys.platform == 'win32':
        print('请在Linux环境下运行该程序')
    else:
        app = QApplication(sys.argv)
        monitor = SystemPerformanceMonitor()
        monitor.show()
        sys.exit(app.exec_())