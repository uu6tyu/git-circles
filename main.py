import sys
from pathlib import Path
from random import randint

from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загружаем интерфейс из файла, лежащего рядом с программой
        uic.loadUi(Path(__file__).with_name("UI.ui"), self)
        self.circles = []  # список окружностей: (x, y, диаметр)
        self.pushButton.clicked.connect(self.add_circle)

    def add_circle(self):
        d = randint(20, 150)
        x = randint(0, self.width() - d)
        y = randint(0, self.height() - d)
        self.circles.append((x, y, d))
        self.update()  # просим Qt перерисовать окно

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor("yellow"))
        for x, y, d in self.circles:
            painter.drawEllipse(x, y, d, d)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Circles()
    window.show()
    sys.exit(app.exec())
