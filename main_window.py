
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    WINDOW_HEIGHT = 700
    WINDOW_WEIGHT = 1000

    def setup_ui(self, main_window):
        # assertion

        main_window.setObjectName("MainWindow")
        main_window.setWindowModality(QtCore.Qt.WindowModal)
        main_window.setEnabled(True)
        main_window.resize(self.WINDOW_WEIGHT, self.WINDOW_HEIGHT)
        self.centralWidget = QtWidgets.QWidget(main_window)
        self.centralWidget.setObjectName("centralWidget")
        main_window.setCentralWidget(self.centralWidget)
        self.toolBar = QtWidgets.QToolBar(main_window)
        self.toolBar.setMovable(True)
        self.toolBar.setObjectName("toolBar")
        main_window.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.addbar = QtWidgets.QAction(main_window)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/iconfinder_plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.addbar.setIcon(icon)
        self.addbar.setObjectName("addbar")
        self.setbar = QtWidgets.QAction(main_window)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/iconfinder_Tile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setbar.setIcon(icon1)
        self.setbar.setObjectName("setbar")
        self.action = QtWidgets.QAction(main_window)
        self.action.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/iconfinder_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action.setIcon(icon2)
        self.action.setObjectName("action")
        self.toolBar.addAction(self.addbar)
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.setbar)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.addbar.setText(_translate("MainWindow", "添加"))
        self.addbar.setToolTip(_translate("MainWindow", "添加文件"))
        self.addbar.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.setbar.setText(_translate("MainWindow", "设置"))
        self.setbar.setToolTip(_translate("MainWindow", "设置"))
        self.action.setText(_translate("MainWindow", "网格布局"))
        self.action.setToolTip(_translate("MainWindow", "网格布局"))
# import r1_rc

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qt_main_window = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setup_ui(qt_main_window)
    qt_main_window.show()
    sys.exit(app.exec_())
