from PyQt5 import QtWidgets, QtWebEngineWidgets  # Don't remove QtWebEngineWidgets!
import sys

from UI import UIScene
from config import LocalConfig
from dataloader import InvestopediaDotComWebDataLoader


def main():
    app = QtWidgets.QApplication([])
    app.Config = LocalConfig('config.json')
    app.DataLoader = InvestopediaDotComWebDataLoader()

    window = UIScene('UI')
    window.resize(1258, 680)
    window.setWindowTitle('Market Observer')
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
