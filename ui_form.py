import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600, 500)
        self.setWindowTitle("Окружности")

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(220, 440, 160, 40)
        self.pushButton.setText("Нарисовать")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())