import sys
from PySide6 import QtWidgets
from src.sqliteui_window import Sqliteui

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Sqliteui()
    window.show()
    sys.exit(app.exec())
