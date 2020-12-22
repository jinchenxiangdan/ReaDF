import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
import fitz


class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.toolbar = self.addToolBar('Exit')

        self.init_window()

    def init_window(self):
        add_action = QAction(QIcon('img/iconfinder_plus.png'), '', self)
        add_action.setShortcut('Ctrl+O')
        # add_action.triggered.connect(qApp.)

        exit_action = QAction(QIcon('img/iconfinder_close.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)

        self.toolbar.addAction(add_action)
        self.toolbar.addAction(exit_action)
        # self.toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 500, 700)
        self.setWindowTitle('Toolbar')
        self.show()

    def _setTableStyle(self):
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
        self.table.customContextMenuRequested.connect(self.generateMenu)

    def read_pdf(self, file_path):
        pdf_file = fitz.open(file_path)