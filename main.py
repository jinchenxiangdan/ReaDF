#!/usr/local/bin/python3
"""
GUI
"""
import sys
from PyQt5.QtWidgets import QApplication

from gui import ReaDF

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReaDF()
    sys.exit(app.exec_())
