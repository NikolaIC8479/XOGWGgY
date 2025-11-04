# 代码生成时间: 2025-11-04 12:08:39
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

"""
用户身份认证程序
该程序使用PyQt5框架创建一个简单的GUI界面，用于用户身份验证。
"""

class UserAuthentication(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('User Authentication')
        self.setGeometry(300, 300, 350, 200)

        # 创建标签、文本框和按钮
        self.label = QLabel('Username:', self)
        self.username = QLineEdit(self)
        self.label2 = QLabel('Password:', self)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.authenticate_button = QPushButton('Authenticate', self)
        self.authenticate_button.clicked.connect(self.authenticate)

        # 布局管理
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.username)
        layout.addWidget(self.label2)
        layout.addWidget(self.password)
        layout.addWidget(self.authenticate_button)
        self.setLayout(layout)

    def authenticate(self):
        """
        用户身份验证函数
        该函数检查用户名和密码是否匹配预设的值
        """
        username = self.username.text()
        password = self.password.text()

        # 预设的用户名和密码
        correct_username = 'admin'
        correct_password = 'password123'

        if username == correct_username and password == correct_password:
            QMessageBox.information(self, 'Success', 'Authentication successful!')
        else:
            QMessageBox.warning(self, 'Error', 'Invalid username or password!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UserAuthentication()
    ex.show()
    sys.exit(app.exec_())