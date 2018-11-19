from PyQt5 import QtWidgets
import calibration_view


class CalibrationVM(calibration_view.Ui_Calibration):
    """
    Compass Calibration.
    """

    def __init__(self, parent):
        self.view = calibration_view.Ui_Calibration.__init__(self)
        self.setupUi(parent)
        self.parent = parent
