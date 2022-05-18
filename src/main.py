import sys
from gui import *

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("WebSurge")
    window = MainWindow()
    sys.exit(app.exec_())

main()