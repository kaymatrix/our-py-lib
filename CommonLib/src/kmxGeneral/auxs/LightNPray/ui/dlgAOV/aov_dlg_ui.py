# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\REPO\SOURCE\SCRIPTS\PYTHON\LightNPray\ui\dlgAOV\aov_dlg_ui.ui'
#
# Created: Tue Dec 14 12:40:05 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 320)
        Dialog.setMinimumSize(QtCore.QSize(400, 320))
        Dialog.setMaximumSize(QtCore.QSize(400, 320))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setMargin(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnCancel = QtGui.QToolButton(self.frame_4)
        self.btnCancel.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnCancel.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCancel.setIcon(icon)
        self.btnCancel.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.btnOK = QtGui.QToolButton(self.frame_4)
        self.btnOK.setMinimumSize(QtCore.QSize(90, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnOK.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOK.setIcon(icon1)
        self.btnOK.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnOK.setObjectName("btnOK")
        self.horizontalLayout_3.addWidget(self.btnOK)
        self.gridLayout.addWidget(self.frame_4, 6, 1, 1, 1)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setStyleSheet("background-color: rgb(94, 198, 103);")
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_3)
        self.gridLayout_5.setMargin(1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.le1 = QtGui.QLineEdit(self.frame_3)
        self.le1.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le1.setFont(font)
        self.le1.setObjectName("le1")
        self.gridLayout_5.addWidget(self.le1, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 1, 1, 1)
        self.frame_7 = QtGui.QFrame(Dialog)
        self.frame_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_2.setMargin(1)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtGui.QListWidget(self.frame_7)
        self.listWidget.setMinimumSize(QtCore.QSize(170, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(170, 16777215))
        self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_7, 1, 0, 6, 1)
        self.matter = QtGui.QFrame(Dialog)
        self.matter.setFrameShape(QtGui.QFrame.NoFrame)
        self.matter.setFrameShadow(QtGui.QFrame.Raised)
        self.matter.setObjectName("matter")
        self.gridLayout_6 = QtGui.QGridLayout(self.matter)
        self.gridLayout_6.setMargin(1)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_9 = QtGui.QLabel(self.matter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)
        self.le3 = QtGui.QLineEdit(self.matter)
        self.le3.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.le3.setFont(font)
        self.le3.setObjectName("le3")
        self.gridLayout_6.addWidget(self.le3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.matter, 3, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btnOK, self.btnCancel)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "HEADER", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOK.setText(QtGui.QApplication.translate("Dialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "MESSAGE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "AOV Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "Available AOVs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Matte Info", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "Apply to Sequence", None, QtGui.QApplication.UnicodeUTF8))
