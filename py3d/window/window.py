import sys
from PyQt5 import QtWidgets,QtCore

class Window():
    def on_button_click(self,x):
        self.que.append(self.names[x])
    def __init__(self):
        super().__init__()
        self.que = []
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle('10 Buttons Example')
        self.window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        layout = QtWidgets.QGridLayout()
        buttons = []
        self.names = ['box','cone','pyramid','sphere']
        for i in range(4):
            button = QtWidgets.QPushButton(self.names[i])
            button.setFixedSize(100, 100)
            button.clicked.connect(lambda _, x=i:self.on_button_click(x))
            buttons.append(button)
            layout.addWidget(button, i // 2, i % 2)
            self.window.setLayout(layout)
            self.window.show()

