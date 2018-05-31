# code = utf-8
__author__ = 'fchao-x'

import sys
import mainWindow
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':

    hostPort = '1.1.1.1:8000'

    app = QApplication(sys.argv)
    ex = mainWindow.Ui_MainWindow()
    sys.exit(app.exec_())