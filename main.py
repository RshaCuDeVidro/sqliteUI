from resources.ui.fodase import Ui_SQLiteUi
from PySide6 import QtWidgets, QtCore, QtGui
import sys

class Sqliteui(QtWidgets.QMainWindow, Ui_SQLiteUi):
    def __init__(self):
        super(Sqliteui, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Sqliteui()
    window.show()
    sys.exit(app.exec())
