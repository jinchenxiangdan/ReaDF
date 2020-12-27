from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    """
    
    Attributes:
            
    """
    
    def __init__(self):
        self._WINDOW_HEIGHT = 700
        self._WINDOW_WEIGHT = 1000

    def setup_ui(self, main_window):
        """
        
        set up the main window with a tool bar.
        
        :param: 
            main_window: 
        :raise:
        """

        # setting main window
        main_window.setObjectName("MainWindow")
        main_window.setWindowModality(QtCore.Qt.WindowModal)
        main_window.setEnabled(True)
        main_window.resize(self._WINDOW_WEIGHT, self._WINDOW_HEIGHT)
        central_widget = QtWidgets.QWidget(main_window)
        central_widget.setObjectName("CentralWidget")
        main_window.setCentralWidget(central_widget)
        # add tool bar

        # add content into tool bar
        #       Open
        #       All Books


    # def retranslate_ui(self, main_window):
    #     _translate = QtCore.QCoreApplication.translate
    #     main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #     self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
    #     self.addbar.setText(_translate("MainWindow", "添加"))
    #     self.addbar.setToolTip(_translate("MainWindow", "添加文件"))
    #     self.addbar.setShortcut(_translate("MainWindow", "Ctrl+A"))
    #     self.setbar.setText(_translate("MainWindow", "设置"))
    #     self.setbar.setToolTip(_translate("MainWindow", "设置"))
    #     self.action.setText(_translate("MainWindow", "网格布局"))
    #     self.action.setToolTip(_translate("MainWindow", "网格布局"))
