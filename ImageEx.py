import sys

from PyQt5.QtWidgets import QLabel,QApplication, QWidget, QPushButton, QVBoxLayout

from PyQt5.QtGui import QPixmap


class QtGUI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label1 = QLabel(self)  # 라벨 생성

        btn4 = QPushButton('Btn4', self)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(btn4)
        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()
        btn4.clicked.connect(self.btn4Function)

    def btn4Function(self):
        self.setWindowTitle("ImageEx")

        pixmap = QPixmap("C:/Users/eoshs/Desktop/디코 이모티콘/꿀벌.png")  # 이미지 관련 클래스 생성 및 이미지 불러오기

        self.label1.setPixmap(pixmap)  # 이미지 관련 클래스와 라벨 연결

        self.resize(pixmap.width() + 20, pixmap.height() + 20)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = QtGUI()

    app.exec_()