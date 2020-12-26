#!/usr/local/bin/python3
"""
GUI
"""
import sys
from PyQt5.QtWidgets import QApplication
from ReaDF import ReaDF

import fitz

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ex = ReaDF()
    # ex.show()
    # sys.exit(app.exec_())
    example_pdf_file_path = "pdf_examples/declaration_of_support.pdf"
    example_pdf_file = fitz.open(example_pdf_file_path)
    print(example_pdf_file.metadata)
    print(example_pdf_file.pageCount)
    print(example_pdf_file.getToC())
    pix_map = example_pdf_file[0].getPixmap()
