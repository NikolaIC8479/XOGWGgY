# 代码生成时间: 2025-10-07 02:10:24
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

"""
音频处理工具
"""

class AudioProcessor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('音频处理工具')
        self.resize(400, 300)

        # 创建布局
        self.layout = QVBoxLayout()

        # 添加标签
        self.label = QLabel('请选择音频文件并播放')
        self.layout.addWidget(self.label)

        # 添加按钮
        self.playButton = QPushButton('播放音频')
        self.playButton.clicked.connect(self.playAudio)
        self.layout.addWidget(self.playButton)

        # 添加视频小部件（用于显示音频波形）
        self.videoWidget = QVideoWidget()
        self.layout.addWidget(self.videoWidget)

        # 设置布局
        self.setLayout(self.layout)

    def playAudio(self):
        # 选择音频文件
        fileName, _ = QFileDialog.getOpenFileName(self, '选择音频文件', '', 'Audio files (*.wav *.mp3)')
        if not fileName:
            return

        # 读取音频文件
        try:
            self.audioData, self.sampleRate = sd.read(fileName, dtype='float64')
        except Exception as e:
            self.label.setText(f'读取音频文件失败：{e}')
            return

        # 创建音频播放器
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent.fromLocalFile(fileName))
        self.player.setVolume(100)
        self.player.play()

        # 更新标签
        self.label.setText(f'播放音频：{fileName}')

        # 更新视频小部件
        self.updateVideoWidget()

    def updateVideoWidget(self):
        # 获取音频波形数据
        if hasattr(self, 'audioData') and hasattr(self, 'sampleRate'):
            audioData = self.audioData
            sampleRate = self.sampleRate
            length = len(audioData)

            # 计算波形数据
            t = np.linspace(0, length / sampleRate, length, False)
            y = np.abs(audioData)

            # 绘制波形
            self.videoWidget.clear()
            pen = QPen(Qt.red)
            pen.setWidth(1)
            self.videoWidget.setPen(pen)
            self.videoWidget.drawLines(t, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AudioProcessor()
    window.show()
    sys.exit(app.exec_())