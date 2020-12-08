from PyQt5 import QtWidgets
import sys

from UI import UIScene


def main():
    app = QtWidgets.QApplication([])
    window = UIScene('UI')
    window.resize(1258, 680)
    window.setWindowTitle('Market Observer')
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
