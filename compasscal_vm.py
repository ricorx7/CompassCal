import compasscal_view


class CompassCalVM(compasscal_view.Ui_RoweTechCompassCal):
    """
    Prediction model.
    """

    def __init__(self, parent):
        compasscal_view.Ui_RoweTechCompassCal.__init__(self)
        self.setupUi(parent)
        self.parent = parent
