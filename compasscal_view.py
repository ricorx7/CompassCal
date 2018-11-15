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
        RoweTechCompassCal.resize(1200, 960)
        self.centralWidget = QtWidgets.QWidget(RoweTechCompassCal)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1182, 942))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        RoweTechCompassCal.setCentralWidget(self.centralWidget)

        self.retranslateUi(RoweTechCompassCal)
        QtCore.QMetaObject.connectSlotsByName(RoweTechCompassCal)

    def retranslateUi(self, RoweTechCompassCal):
        _translate = QtCore.QCoreApplication.translate
        RoweTechCompassCal.setWindowTitle(_translate("RoweTechCompassCal", "MainWindow"))
        self.label.setText(_translate("RoweTechCompassCal", "Rowe Technologies Inc. Compass Calibration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RoweTechCompassCal = QtWidgets.QMainWindow()
    ui = Ui_RoweTechCompassCal()
    ui.setupUi(RoweTechCompassCal)
    RoweTechCompassCal.show()
    sys.exit(app.exec_())

