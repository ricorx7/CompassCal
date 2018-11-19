# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calibration_view.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calibration(object):
    def setupUi(self, Calibration):
        Calibration.setObjectName("Calibration")
        Calibration.resize(871, 611)
        self.progressBar = QtWidgets.QProgressBar(Calibration)
        self.progressBar.setGeometry(QtCore.QRect(310, 330, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Calibration)
        self.label.setGeometry(QtCore.QRect(340, 233, 141, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Calibration)
        QtCore.QMetaObject.connectSlotsByName(Calibration)

    def retranslateUi(self, Calibration):
        _translate = QtCore.QCoreApplication.translate
        Calibration.setWindowTitle(_translate("Calibration", "Form"))
        self.label.setText(_translate("Calibration", "Compass Calibration"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calibration = QtWidgets.QWidget()
    ui = Ui_Calibration()
    ui.setupUi(Calibration)
    Calibration.show()
    sys.exit(app.exec_())

