from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QComboBox
from src.utils import list_tables, open_database
from src.new_db_window import NewDbWindow
from resources.ui.ui_sqliteui import Ui_SQLiteUi

class Sqliteui(QtWidgets.QMainWindow, Ui_SQLiteUi):
    def __init__(self):
        super(Sqliteui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_sql)
        self.comboBox.setEnabled(False)
        self.comboBox.currentTextChanged.connect(self.comboBoxTableChanged)
        
        self.cursor = None
        self.con = None

        self.pushButton_2_new.clicked.connect(self.new_sql)

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

    def open_sql(self):
        self.comboBox.clear()
        db_path = QFileDialog.getOpenFileNames(self,"Selecione um","/home","Sqlite (*.db *.sql *.sqlite3 *.sqlite)")
        
        if db_path == "": # pressionou cancel
            return
        db_path = db_path[0][0]
        
        self.con, self.cursor = open_database(db_path)  # Use a função do utils
        
        tables = list_tables(self.cursor)  # Use a função do utils
        self.comboBox.addItems(tables)
        self.comboBox.setEnabled(True)

    def new_sql(self):
        self.nova_janela = NewDbWindow()
        self.nova_janela.show()