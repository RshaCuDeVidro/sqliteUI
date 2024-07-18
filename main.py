from resources.ui.fodase import Ui_SQLiteUi
from PySide6 import QtWidgets, QtCore, QtGui
import sys
import sqlite3
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QComboBox
                                           
class Sqliteui(QtWidgets.QMainWindow, Ui_SQLiteUi):
    def __init__(self):
        super(Sqliteui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_sql)
        self.comboBox.setEnabled(False)
        self.comboBox.currentTextChanged.connect(self.comboBoxTableChanged)
        

        ###gambiarras logo abaixo###
        self.cursor = None
        self.con = None

    def comboBoxTableChanged(self, index):
        if self.cursor is None or self.con is None:
            print("sem conexão ou sem cursor")
            return

        self.cursor.execute(f'SELECT * FROM {index}')
        col_names = [description[0] for description in self.cursor.description]

        
        rows = self.cursor.fetchall()

        

        
        self.tableWidget_2.setRowCount(len(rows))
        self.tableWidget_2.setColumnCount(len(col_names))

        
        self.tableWidget_2.setHorizontalHeaderLabels(col_names)

        
        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget_2.setItem(row_num, col_num, item)

        
        self.tableWidget_2.resizeColumnsToContents()

        print(index)
        pass

    def list_tables(self, cur):
        monkey = []
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        piroca = cur.fetchall()
        print(piroca)
        for pussy in piroca:
            monkey.append(pussy[0])
        
        return monkey

    def open_sql(self):
        print('aa')
        self.comboBox.clear()
        db_path = QFileDialog.getOpenFileNames(self,"Selecione um","/home","Sqlite (*.db *.sql *.sqlite3 *.sqlite)")
        db_path = db_path[0][0]
        
        

        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()
        

        tables = self.list_tables(self.cursor)
        self.comboBox.addItems(tables)
        self.comboBox.setEnabled(True)

        
        #cursor.execute('SELECT * FROM users_use')
        #col_names = [description[0] for description in cursor.description]

        
        #rows = cursor.fetchall()

        #connection.close()

        
        #self.tableWidget_2.setRowCount(len(rows))
        #self.tableWidget_2.setColumnCount(len(col_names))

        
        #self.tableWidget_2.setHorizontalHeaderLabels(col_names)

        
        #for row_num, row_data in enumerate(rows):
        #    for col_num, data in enumerate(row_data):
        #        item = QTableWidgetItem(str(data))
        #        self.tableWidget_2.setItem(row_num, col_num, item)

        
        #self.tableWidget_2.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Sqliteui()
    window.show()
    sys.exit(app.exec())
