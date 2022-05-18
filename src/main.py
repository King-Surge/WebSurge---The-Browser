import sys
from gui import MainWindow

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("WebSurge")
    window = MainWindow()
    sys.exit(app.exec_())

main()