#!/usr/bin/python3
"""
GUI
"""
import sys
from PyQt5.QtWidgets import QApplication
from ReaDF import ReaDF

import fitz

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ReaDF()
    ex.show()
    sys.exit(app.exec_())

