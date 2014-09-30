'''
Created on Sep 28, 2014 Sun - 21:08:20

@author: Kumaryes
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from user_interface.win_main import Ui_MainWindow
import sys
import os


class WinMain(QtWidgets.QMainWindow, Ui_MainWindow):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent = parent
        self.connectSignalSlots()

    def connectSignalSlots(self):
        self.pushButton.clicked.connect(self.parent.btnClickHere)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    m = WinMain(app)
    m.show()
    sys.exit(app.exec_())
    
