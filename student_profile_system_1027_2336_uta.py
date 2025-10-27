# 代码生成时间: 2025-10-27 23:36:09
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

"""
学生画像系统
一个使用PyQt5框架创建的简单GUI应用程序，用于输入和展示学生信息。
"""

class StudentProfileSystem(QWidget):
    """
    学生画像系统的主窗口类。
    """
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """
        初始化用户界面。
        """
        # 设置窗口标题和大小
        self.setWindowTitle('学生画像系统')
        self.setGeometry(100, 100, 300, 200)

        # 创建布局
        layout = QVBoxLayout()

        # 创建标签和输入框
        self.name_label = QLabel('姓名：')
        self.name_edit = QLineEdit()
        self.age_label = QLabel('年龄：')
        self.age_edit = QLineEdit()

        # 创建按钮
        self.submit_button = QPushButton('提交')
        self.submit_button.clicked.connect(self.submit_student_info)

        # 将组件添加到布局
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_edit)
        layout.addWidget(self.submit_button)

        # 设置布局为窗口的主布局
        self.setLayout(layout)

    def submit_student_info(self):
        """
        提交学生信息的处理函数。
        """
        try:
            name = self.name_edit.text().strip()
            age = self.age_edit.text().strip()
            if not name or not age:
                raise ValueError('姓名和年龄不能为空！')
            age = int(age)
            if age <= 0:
                raise ValueError('年龄必须大于0！')
            # 这里可以添加将学生信息保存到数据库的代码
            print(f'学生信息已提交：姓名：{name}，年龄：{age}')
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    # 创建应用程序实例
    app = QApplication(sys.argv)
    # 创建窗口实例
    window = StudentProfileSystem()
    # 显示窗口
    window.show()
    # 运行应用程序
    sys.exit(app.exec_())