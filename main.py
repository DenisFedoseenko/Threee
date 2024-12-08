import sys
import random
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QMainWindow, QApplication
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.draw_random_circle)

        self.canvas = QtGui.QPainter(self)

    def draw_random_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        self.last_circle = (x, y, diameter)

        self.update()

    def paintEvent(self, event):
        if hasattr(self, 'last_circle'):
            painter = QtGui.QPainter(self)
            painter.setBrush(QtGui.QColor("yellow"))
            x, y, diameter = self.last_circle
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
