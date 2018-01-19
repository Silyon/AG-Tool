# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './windows/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1032, 680)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(8, 616, 71, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(8, 408, 1016, 193))
        self.tableView.setStyleSheet("border-style: none;")
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setStyleSheet("selection-color:rgb(255,255,255); \n"
"selection-background-color:rgb(100,149,237);\n"
"border-bottom: 1px;\n"
"border-bottom-color: grey;\n"
"border-bottom-style: outset;\n"
"width: 50px;\n"
"")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("text-align: center;\n"
"width: 200px;")
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionScan_Seasonal_Anime = QtWidgets.QAction(MainWindow)
        self.actionScan_Seasonal_Anime.setObjectName("actionScan_Seasonal_Anime")
        self.menuFile.addAction(self.actionScan_Seasonal_Anime)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AG Tool"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionScan_Seasonal_Anime.setText(_translate("MainWindow", "Scan Seasonal Anime (Ctrl + S)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

