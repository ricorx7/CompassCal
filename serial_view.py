# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_view.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SerialView(object):
    def setupUi(self, SerialView):
        SerialView.setObjectName("SerialView")
        SerialView.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(SerialView)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 40, 251, 181))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.portComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.portComboBox.setObjectName("portComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.portComboBox)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.baudComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.baudComboBox.setObjectName("baudComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.baudComboBox)
        self.connectButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.connectButton.setStyleSheet("background: rgb(85, 85, 255);")
        self.connectButton.setObjectName("connectButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.connectButton)
        self.disconnectButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.disconnectButton.setStyleSheet("background: rgb(255, 0, 0)")
        self.disconnectButton.setObjectName("disconnectButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.disconnectButton)

        self.retranslateUi(SerialView)
        QtCore.QMetaObject.connectSlotsByName(SerialView)

    def retranslateUi(self, SerialView):
        _translate = QtCore.QCoreApplication.translate
        SerialView.setWindowTitle(_translate("SerialView", "Form"))
        self.label.setText(_translate("SerialView", "Port"))
        self.label_2.setText(_translate("SerialView", "Baud Rate"))
        self.connectButton.setText(_translate("SerialView", "Connect"))
        self.disconnectButton.setText(_translate("SerialView", "Disconnect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SerialView = QtWidgets.QWidget()
    ui = Ui_SerialView()
    ui.setupUi(SerialView)
    SerialView.show()
    sys.exit(app.exec_())

