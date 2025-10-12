# 代码生成时间: 2025-10-13 01:58:25
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTextEdit, QMenuBar, QFileDialog
from PyQt5.QtGui import QTextCharFormat, QColor
from PyQt5.QtCore import Qt

"""
A simple rich text editor using PyQt5.
"""

class RichTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the main window
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Rich Text Editor')

        # Create a QTextEdit widget for editing
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Create a menu bar and add actions for file operations
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        # File menu
        fileMenu = self.menuBar.addMenu('File')
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        # Format menu for text formatting
        formatMenu = self.menuBar.addMenu('Format')
        # Add actions for font styling here...

    def openFile(self):
        # Open a file dialog to choose a file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if fileName:
            try:
                with open(fileName, 'r') as f:
                    self.textEdit.setPlainText(f.read())
            except Exception as e:
                print(f'Failed to open file: {e}')

    def saveFile(self):
        # Open a file dialog to save a file
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if fileName:
            try:
                with open(fileName, 'w') as f:
                    f.write(self.textEdit.toPlainText())
            except Exception as e:
                print(f'Failed to save file: {e}')

    def about(self):
        pass  # Implement an about dialog or information

    def closeEvent(self, event):
        # Handle closing of the application
        event.accept()

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = RichTextEditor()
    editor.show()
    sys.exit(app.exec_())