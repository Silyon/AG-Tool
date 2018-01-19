from PyQt5 import QtCore, QtGui, QtWidgets
   
header = ['#', 'Title', 'Producer', 'Type', 'Start Date']           
tabledata = [["0", "No File Selected", "N/A", "N/A", "N/A"]]
                
                
class HeaderView(QtWidgets.QHeaderView):
    def __init__(self, parent):
        QtWidgets.QHeaderView.__init__(self, QtCore.Qt.Horizontal, parent)
        self.model = TableModel(header, tabledata)
        self.setModel(self.model)
        
        self.setSectionResizeMode(2)
        self.resizeSection(0, 30)
        self.resizeSection(1, 300)
        self.resizeSection(2, 300)
        self.resizeSection(3, 60)
        self.resizeSection(4, 300)
        self.setSectionsClickable(True)

                
class TableModel(QtCore.QAbstractTableModel):
    
    def __init__(self, headers, content):
        QtCore.QAbstractTableModel.__init__(self)
        super(TableModel, self).__init__()
        
        self.headers = headers
        self.content = content
        
    def rowCount(self, parent=None):
        return len(self.content)
    
    def columnCount(self, parent=None):
        return len(self.content[0])
    
            
    def data(self, index, role=None):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self.content[row][col]
            return value
        
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
    

    def headerData(self, section, orientation, role=None):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]
        