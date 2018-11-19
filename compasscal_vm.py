from PyQt5 import QtGui, QtWidgets
import compasscal_view
from serial_vm import SerialVM
from calibration_vm import CalibrationVM

class CompassCalVM(compasscal_view.Ui_RoweTechCompassCal):
    """
    Prediction model.
    """

    def __init__(self, parent):
        self.view = compasscal_view.Ui_RoweTechCompassCal.__init__(self)
        self.setupUi(parent)
        self.parent = parent

        # Setup Menu to open serial dialog
        self.actionConnectSerial.triggered.connect(self.serial_port_view)
        self.actionHome.triggered.connect(self.home_view)

        self.cal = CalibrationVM(self.parent)

        self.serial_port = None

    def serial_port_view(self):
        self.parent.hide()
        self.serial_port = SerialVM(self.parent)
        self.serial_port.parent.show()

    def home_view(self):
        self.parent.hide()
        #self.cal.parent.hide()
        self.cal.parent.show()
