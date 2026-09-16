import sys
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit )
from PyQt6.QtGui import QColor,QPalette
class FiestaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('gay el que lo lea')
        self.setMinimumSize(300,200)
        self.setMaximumSize(500,400)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("green") )
        self.setPalette(palette)
        boton = QPushButton('pulsa')
        etiqueta = QLabel("ola a todas")
        self.setCentralWidget(boton)
        self.setCentralWidget(etiqueta)
        self.show()



if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiesta = FiestaPrincipal()
    aplicacion.exec()