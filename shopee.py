from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tell_keyword = QtWidgets.QLabel(self.centralwidget)
        self.tell_keyword.setGeometry(QtCore.QRect(30, 20, 167, 26))
        self.tell_keyword.setMaximumSize(QtCore.QSize(191, 16777215))
        font = QtGui.QFont()
        font.setFamily("有愛ウォークラフト角ゴシック CN")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tell_keyword.setFont(font)
        self.tell_keyword.setObjectName("tell_keyword")
        self.tell_pages = QtWidgets.QLabel(self.centralwidget)
        self.tell_pages.setGeometry(QtCore.QRect(30, 60, 148, 26))
        self.tell_pages.setMaximumSize(QtCore.QSize(191, 16777215))
        font = QtGui.QFont()
        font.setFamily("有愛ウォークラフト角ゴシック CN")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.tell_pages.setFont(font)
        self.tell_pages.setObjectName("tell_pages")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(30, 98, 429, 33))
        font = QtGui.QFont()
        font.setFamily("有愛ウォークラフト角ゴシック CN")
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.state_table = QtWidgets.QTextBrowser(self.centralwidget)
        self.state_table.setGeometry(QtCore.QRect(30, 137, 429, 191))
        font = QtGui.QFont()
        font.setFamily("有愛ウォークラフト角ゴシック CN")
        font.setPointSize(11)
        self.state_table.setFont(font)
        self.state_table.setObjectName("state_table")
        self.keyword_input = QtWidgets.QLineEdit(self.centralwidget)
        self.keyword_input.setGeometry(QtCore.QRect(200, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("有愛ウォークラフト角ゴシック CN")
        font.setPointSize(11)
        self.keyword_input.setFont(font)
        self.keyword_input.setText("")
        self.keyword_input.setObjectName("keyword_input")
        self.pages_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pages_input.setGeometry(QtCore.QRect(200, 60, 261, 31))
        font = QtGui.QFont()
        font.setFamily("有愛ウォークラフト角ゴシック CN")
        font.setPointSize(11)
        self.pages_input.setFont(font)
        self.pages_input.setText("")
        self.pages_input.setObjectName("pages_input")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tell_keyword.setText(_translate("MainWindow", "請輸入商品關鍵字："))
        self.tell_pages.setText(_translate("MainWindow", "請輸入搜尋頁數："))
        self.start_button.setText(_translate("MainWindow", "開   始"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())