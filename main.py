import sys
from windowSetups import MainWin
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWin()
    
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()