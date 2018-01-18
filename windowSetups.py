import sys
sys.path.append('./windows')
sys.path.append('../imports')

from PyQt5 import QtCore, QtGui, QtWidgets
from windows import mainWindow, seasonScanner
from imports import seasonModule
from imports import xmlToList as XL
import datetime


class MainWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.scannerWin = None
        self.setupSignals()
        self.setupListView()
        
    def setupSignals(self):
        self.ui.actionScan_Seasonal_Anime.triggered.connect(self.openScanner)
        self.ui.pushButton.clicked.connect(self.closeButton)
    
    def closeButton(self):
        self.close()
    
    def openScanner(self):
        if not self.scannerWin:
            self.scannerWin = ScannerWin()
        
        if self.scannerWin.isVisible():
            print("Hiding")
            self.scannerWin.close()
        else:
            print("Showing")
            self.scannerWin.show()
            
    def setupListView(self):
        xmlList = XL.xmlToList("./res/saved_seasons/Winter2018.xml")
        model = QtGui.QStandardItemModel(self.ui.listView)
        
        for i in xmlList:
            item = QtGui.QStandardItem(i.title)
            model.appendRow(item)
            
        self.ui.listView.setModel(model)
    
class ScannerWin(QtWidgets.QMainWindow):
    seasonSelect = "Winter"
    yearSelect = datetime.datetime.now().year
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = seasonScanner.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupSignals()
        self.setupYearList()
        
    def setupSignals(self):
        self.ui.comboBox.activated.connect(self.handleActivated1)
        self.ui.comboBox_2.activated.connect(self.handleActivated2)
        self.ui.pushButton.clicked.connect(self.on_click1)
        self.ui.pushButton_2.clicked.connect(self.on_click2)
        
    def setupYearList(self):
        for i in range(datetime.datetime.now().year, 1916, -1):
            self.ui.comboBox_2.addItem(str(i))
        
    def handleActivated1(self, index):
        self.seasonSelect = self.ui.comboBox.itemText(index)
    
    def handleActivated2(self, index):
        self.yearSelect = self.ui.comboBox_2.itemText(index)
    
    def on_click1(self):
        self.season = str(self.seasonSelect) + " " + str(self.yearSelect)
        print("Selected season: " + self.season)
        self.dump = "y"
        
        seasonModule.main(self.season.lower(), self.dump)
        print(seasonModule.toPrint.encode('utf-8'))
        self.ui.textBrowser.setText(seasonModule.theAnis.encode('utf-8'))
        
    def on_click2(self):
        print("Hiding")
        self.close()