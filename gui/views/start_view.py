from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette


def show_view():
    app = QApplication([])
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.ButtonText, Qt.red)
    app.setPalette(palette)
    app.setStyleSheet("QPushButton { margin-right: 10ex; margin-left: 10ex; }")
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QLabel('Choose platform to use'))
    layout.addWidget(QPushButton('Open Web Application'))
    layout.addWidget(QPushButton('Open Desktop Application'))
    window.setLayout(layout)
    window.show()
    app.exec()

show_view()