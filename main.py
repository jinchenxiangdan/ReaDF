#!/usr/local/bin/python3
"""
GUI
"""
import sys
from PyQt5.QtWidgets import QApplication

from gui import GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())
