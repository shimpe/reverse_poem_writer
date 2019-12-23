# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iface.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1085, 735)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left = QtWidgets.QPlainTextEdit(Dialog)
        self.left.setObjectName("left")
        self.horizontalLayout_2.addWidget(self.left)
        self.right = QtWidgets.QPlainTextEdit(Dialog)
        self.right.setEnabled(True)
        self.right.setObjectName("right")
        self.horizontalLayout_2.addWidget(self.right)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.load = QtWidgets.QPushButton(Dialog)
        self.load.setObjectName("load")
        self.horizontalLayout.addWidget(self.load)
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setObjectName("save")
        self.horizontalLayout.addWidget(self.save)
        self.closebtn = QtWidgets.QPushButton(Dialog)
        self.closebtn.setObjectName("closebtn")
        self.horizontalLayout.addWidget(self.closebtn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reverse Poem Writer"))
        self.load.setText(_translate("Dialog", "Load"))
        self.save.setText(_translate("Dialog", "Save"))
        self.closebtn.setText(_translate("Dialog", "Close"))
