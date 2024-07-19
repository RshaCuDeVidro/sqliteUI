from PySide6 import QtWidgets
from resources.ui.new_db import Ui_Tabela

class NewDbWindow(QtWidgets.QWidget, Ui_Tabela):
    def __init__(self):
        super(NewDbWindow, self).__init__()
        self.setupUi(self)