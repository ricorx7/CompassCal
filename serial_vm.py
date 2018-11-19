from PyQt5 import QtWidgets
import serial_view


class SerialVM(serial_view.Ui_SerialView):
    """
    Setup serial communication.
    """

    def __init__(self, parent):
        self.view = serial_view.Ui_SerialView.__init__(self)
        self.setupUi(parent)
        self.parent = parent
