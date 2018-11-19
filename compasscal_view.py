# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compasscal_view.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RoweTechCompassCal(object):
    def setupUi(self, RoweTechCompassCal):
        RoweTechCompassCal.setObjectName("RoweTechCompassCal")
        RoweTechCompassCal.resize(905, 571)
        self.centralWidget = QtWidgets.QWidget(RoweTechCompassCal)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        RoweTechCompassCal.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(RoweTechCompassCal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 905, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuPort = QtWidgets.QMenu(self.menuBar)
        self.menuPort.setObjectName("menuPort")
        RoweTechCompassCal.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(RoweTechCompassCal)
        self.toolBar.setObjectName("toolBar")
        RoweTechCompassCal.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtWidgets.QAction(RoweTechCompassCal)
        self.actionExit.setObjectName("actionExit")
        self.actionPort = QtWidgets.QAction(RoweTechCompassCal)
        self.actionPort.setObjectName("actionPort")
        self.actionBaud = QtWidgets.QAction(RoweTechCompassCal)
        self.actionBaud.setObjectName("actionBaud")
        self.actionConnectSerial = QtWidgets.QAction(RoweTechCompassCal)
        self.actionConnectSerial.setObjectName("actionConnectSerial")
        self.actionHome = QtWidgets.QAction(RoweTechCompassCal)
        self.actionHome.setObjectName("actionHome")
        self.menuFile.addAction(self.actionHome)
        self.menuFile.addAction(self.actionExit)
        self.menuPort.addAction(self.actionPort)
        self.menuPort.addAction(self.actionBaud)
        self.menuPort.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuPort.menuAction())
        self.toolBar.addAction(self.actionConnectSerial)

        self.retranslateUi(RoweTechCompassCal)
        QtCore.QMetaObject.connectSlotsByName(RoweTechCompassCal)

    def retranslateUi(self, RoweTechCompassCal):
        _translate = QtCore.QCoreApplication.translate
        RoweTechCompassCal.setWindowTitle(_translate("RoweTechCompassCal", "MainWindow"))
        self.menuFile.setTitle(_translate("RoweTechCompassCal", "File"))
        self.menuPort.setTitle(_translate("RoweTechCompassCal", "Connect"))
        self.toolBar.setWindowTitle(_translate("RoweTechCompassCal", "toolBar"))
        self.actionExit.setText(_translate("RoweTechCompassCal", "Exit"))
        self.actionPort.setText(_translate("RoweTechCompassCal", "Port"))
        self.actionBaud.setText(_translate("RoweTechCompassCal", "Baud"))
        self.actionConnectSerial.setText(_translate("RoweTechCompassCal", "Connect Serial"))
        self.actionConnectSerial.setIconText(_translate("RoweTechCompassCal", "Serial Port"))
        self.actionHome.setText(_translate("RoweTechCompassCal", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoweTechCompassCal = QtWidgets.QMainWindow()
    ui = Ui_RoweTechCompassCal()
    ui.setupUi(RoweTechCompassCal)
    RoweTechCompassCal.show()
    sys.exit(app.exec_())

