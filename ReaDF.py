"""
Author: Shawn Jin
Purpose:
"""


import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, \
        QApplication, QPushButton, QFrame, QAction, QFileDialog, QHBoxLayout, QTableWidget, QTableWidgetItem, \
        QLabel, QMenu, QAbstractItemView
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import QSize, Qt
from main_window import MainWindow

import fitz


def init_tool_bar(main_window):
    """

    Initial tool bar of a main window. Add {} into the tool bar.

    :param main_window: a QMainWindow object
    :return:
    """
    # set up a empty tool bar
    tool_bar = QtWidgets.QToolBar(main_window)
    tool_bar.setMovable(True)
    tool_bar.setObjectName("ToolBar")
    main_window.addToolBar(QtCore.Qt.TopToolBarArea, tool_bar)
    open_file_button = QtWidgets.QAction(main_window)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("img/iconfinder_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
    open_file_button.setIcon(icon)
    open_file_button.setObjectName("OpenFile")
    set_bar = QtWidgets.QAction(main_window)
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap("img/iconfinder_Tile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    set_bar.setIcon(icon1)
    set_bar.setObjectName("setbar")
    action = QtWidgets.QAction(main_window)
    action.setCheckable(True)
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap("img/iconfinder_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    action.setIcon(icon2)
    action.setObjectName("action")
    tool_bar.addAction(open_file_button)
    tool_bar.addAction(action)
    tool_bar.addAction(set_bar)


class ReaDF(QMainWindow, MainWindow):

    _TITLE = "ReaDF"
    _FILE_PATH = "pdf_examples/"

    def __init__(self, parent=None):
        """

        Initial ReaDF window, icon,

        :param parent:
        """
        super(ReaDF, self).__init__(parent)
        self.setup_ui(self)
        init_tool_bar(self)

        ##################################################################
        # test
        ##################################################################
        print(fitz.__doc__)
        example_pdf_file_path = "pdf_examples/declaration_of_support.pdf"
        example_pdf_file = fitz.open(example_pdf_file_path)
        print(example_pdf_file.metadata)
        print(example_pdf_file.pageCount)
        print(example_pdf_file.getToC())
        pix_map = example_pdf_file[0].getPixmap()
        ##################################################################

        # self.y = 0
        # self.x = 0
        self.setWindowIcon(QIcon('img/book.png'))
        self.setWindowTitle(self._TITLE)
        # self.screen = QDesktopWidget().screenGeometry()
        # self.setup_ui(self)
        # self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        # self.setContextMenuPolicy(Qt.NoContextMenu)
        # # self.setFixedSize(self.screen.width(), self.screen.height())
        # self.table = QTableWidget()
        # self.setCentralWidget(self.table)
        # self.init_ui()
        # self.book_list = []

    def filter_book(self, fname):
        if not fname:
            return False
        if fname not in self.book_list:
            self.book_list.append(fname)
            return True
        return False

    def read_files(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Open files", './', '(*.pdf)')
        return fname

    def open(self):
        fname = self.read_files()
        if self.filter_book(fname):
            self.setIcon(fname)

    def set_table_style(self):
        # 开启水平与垂直滚轴
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # 设置 5 行 8 列 的表格
        self.table.setColumnCount(8)
        self.table.setRowCount(5)
        # 设置标准宽度
        self.width = self.screen.width() // 8
        # 设置单元格的宽度
        for i in range(8):
            self.table.setColumnWidth(i, self.width)
        # 设置单元格的高度
        # 设置纵横比为 4 : 3
        for i in range(5):
            self.table.setRowHeight(i, self.width * 4 // 3)
        # 隐藏标题栏
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        # 禁止编辑
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 不显示网格线
        self.table.setShowGrid(False)
        # 将单元格绑定右键菜单
        # 点击单元格，调用 self.generateMenu 函数
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.generate_menu)

    def read_pdf(self, file_path):
        pdf_file = fitz.open(file_path)
        # TODO: add custom setting on naming files
        title = file_path.split('/' or '\\')[-1].replace('.pdf', '')


    def setIcon(self, file_name):
        pdf_file = fitz.open(file_name)
        cover = render_pdf_page(pdf_file, True)
        label = QLabel(self)
        label.setScaledContents(True)
        label.setPixmap(QPixmap(cover))
        self.table.setCellWidget(self.x, self.y, label)

        del label
        self.crow, self.ccol = self.x, self.y
        if (not self.y % 7) and (self.y):
            self.x += 1
            self.y = 0
        else:
            self.y += 1

    def generate_menu(self, pos):
        row_num = col_num = -1
        # 获取选中的单元格的行数以及列数
        for i in self.table.selectionModel().selection().indexes():
            row_num = i.row()
            col_num = i.column()
        # 若选取的单元格中有元素，则支持右键菜单
        if (row_num < self.crow) or (row_num == self.crow and col_num <= self.ccol):
            menu = QMenu()
            item1 = menu.addAction('开始阅读')
            item2 = menu.addAction('删除图书')
            # 获取选项
            action = menu.exec_(self.table.mapToGlobal(pos))
            if action == item1:
                index = row_num * 8 + col_num
                fname = self.book_list[index]
                if fname not in self.read_list and len(self.read_list) < 2:
                    self.read_list.append(fname)
                    self.read_book(fname)
            elif action == item2:
                self.delete_book(row_num, col_num)


def render_pdf_page(pdf_page, for_cover=False):
    zoom_matrix = fitz.Matrix(4, 4)
    if for_cover:
        zoom_matrix = fitz.Matrix(1, 1)

    page_pixmap = pdf_page.getPixmap(
        matrix=zoom_matrix,
        alpha=False
    )
    image_format = QtGui.QImage.Format_RGB888
    page_qimg = QtGui.QImage(
        page_pixmap.samples,
        page_pixmap.width,
        page_pixmap.height,
        page_pixmap.stride,
        image_format)
    pixmap = QtGui.QPixmap()
    pixmap.convertFromImage(page_qimg)
    return pixmap
