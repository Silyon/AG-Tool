import sys
sys.path.append('./windows')
sys.path.append('../imports')

from PyQt5 import QtCore, QtGui, QtWidgets
from windows import mainWindow, seasonScanner
from imports import seasonModule
from imports import xmlToList as XL
from imports import CTableView
import datetime


class MainWin(QtWidgets.QMainWindow):
    filename = ""
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = mainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.scannerWin = None
        self.setupSignals()
        self.setupTableView()
        
    def setupSignals(self):
        self.ui.actionScan_Seasonal_Anime.triggered.connect(self.openScanner)
        self.ui.pushButton_2.clicked.connect(self.openFile)
        self.ui.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+S"), self)
        self.ui.shortcut.activated.connect(self.openScanner)
        
        
    def openFile(self):
        filters = "*.xml"
        selected_filter = "XML Files (*.xml)"
        self.filename, fill = QtWidgets.QFileDialog.getOpenFileName(self, "Open XML File", filters, selected_filter)
        print("Opened: " + self.filename)
        
        self.updateTable()

    def openScanner(self):
        if not self.scannerWin:
            self.scannerWin = ScannerWin()
        
        if self.scannerWin.isVisible():
            print("Hiding")
            self.scannerWin.close()
        else:
            print("Showing")
            self.scannerWin.show()
            
    def updateTable(self):
        xmlMatrix = XL.xmlToMatrix(self.filename)
        model2 = CTableView.TableModel(CTableView.header, xmlMatrix)
        self.ui.tableView.setModel(model2)
        self.ui.tableView.update()

        
    def setupTableView(self):
        if self.filename == "":
            model = CTableView.TableModel(CTableView.header, CTableView.tabledata)
            self.ui.tableView.setModel(model)
            
        self.ui.tableView.setShowGrid(False)
        
        hview = CTableView.HeaderView(self.ui.tableView)
        self.ui.tableView.setHorizontalHeader(hview)
        self.ui.tableView.verticalHeader().hide()
        
        self.ui.tableView.setAlternatingRowColors(True)
    
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
        self.ui.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self)
        self.ui.shortcut.activated.connect(self.on_click2)
        
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