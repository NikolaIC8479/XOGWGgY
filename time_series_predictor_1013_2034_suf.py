# 代码生成时间: 2025-10-13 20:34:40
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import pyqtSlot
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 时间序列预测器类
class TimeSeriesPredictor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('时间序列预测器')
        self.resize(600, 400)

        # 创建布局
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)

        # 创建输入框和按钮
        self.input_text = QLineEdit()
        self.predict_button = QPushButton('预测')
        self.output_text = QTextEdit()

        # 将控件添加到布局中
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.predict_button)
        self.layout.addWidget(self.output_text)

        # 绑定按钮点击事件
        self.predict_button.clicked.connect(self.predict)

    def predict(self):
        # 获取输入数据
        data = self.input_text.text()
        try:
            # 将输入数据转换为浮点数列表
            data = [float(x) for x in data.split(',')]
            # 将数据转换为时间序列
            time_series = np.array(data).reshape(-1, 1)

            # 分割数据集
            X_train, X_test, y_train, y_test = train_test_split(time_series, time_series, test_size=0.2, random_state=42)

            # 创建并训练模型
            model = LinearRegression()
            model.fit(X_train, y_train)

            # 进行预测
            y_pred = model.predict(X_test)

            # 计算均方误差
            mse = mean_squared_error(y_test, y_pred)

            # 显示结果
            result = f'预测结果: {y_pred}
均方误差: {mse}'
            self.output_text.setText(result)
        except ValueError as e:
            # 错误处理
            self.output_text.setText(f'输入错误: {str(e)}')

# 主函数
def main():
    app = QApplication(sys.argv)
    window = TimeSeriesPredictor()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()