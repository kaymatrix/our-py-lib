# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Kumaresan\Code\Python\PPG\src\user_interface\wgt_form1_general.ui'
#
# Created: Mon Sep 22 07:33:03 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(526, 416)
        self.gridLayout_2 = QtWidgets.QGridLayout(form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(form)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(2, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(121, 16))
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_6.addWidget(self.radioButton, 0, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_6.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 3, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(form)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_5.setContentsMargins(2, 0, 0, 6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setMinimumSize(QtCore.QSize(121, 16))
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_5.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 2)
        self.widget = QtWidgets.QWidget(form)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(2, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(121, 16))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 2)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.label_2.setText(_translate("form", "Author"))
        self.groupBox.setTitle(_translate("form", "Project Type:"))
        self.radioButton.setText(_translate("form", "PyQt - Windows Application"))
        self.radioButton_2.setText(_translate("form", "Python - Commandline Application"))
        self.label_3.setText(_translate("form", "Code Location"))
        self.label.setText(_translate("form", "Project Name"))

