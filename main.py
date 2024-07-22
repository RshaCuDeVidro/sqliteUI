from resources.ui.ui_sqliteui import Ui_SQLiteUi
from PySide6 import QtWidgets, QtCore, QtGui
import sys
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem, QComboBox, QTreeWidgetItem
from src.utils import list_tables, open_database
from src.new_db_window import NewDbWindow

class Sqliteui(QtWidgets.QMainWindow, Ui_SQLiteUi):
    def __init__(self):
        super(Sqliteui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_sql)
        self.comboBox.setEnabled(False)
        self.comboBox.currentTextChanged.connect(self.comboBoxTableChanged)
        self.pushButton_2_new.clicked.connect(self.new_sql)

        self.cursor = None
        self.con = None

        #paginação
        self.current_page = 0
        self.itemPorPage = 10
        
        self.pushButton_pagDps.clicked.connect(self.next_page)
        self.pushButton_pagAntes.clicked.connect(self.prev_page)       


    def next_page(self):
        if (self.current_page + 1) * self.itemPorPage < len(self.rows):
            self.current_page += 1
            self.update_table()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_table()



    def SQLStructure(self):
        """
        Fazer a estutura do banco usando aquele QTreeWidget :>
		"""
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

        tables = [row[0] for row in self.cursor.fetchall()]

        for table in tables:

            table_item = QTreeWidgetItem([table, "", ""])
            self.treeWidget.addTopLevelItem(table_item)
            self.cursor.execute(f"PRAGMA table_info({table})")
            """
			sqlite> .tables
			users      users_use
			sqlite> pragma table_info(users)  ## <-- Exemplo de Pragma table_info
			   ...> ;
			0|id|INTEGER|0||1
			1|userid|TEXT|0||0
			2|username|TEXT|0||0
			3|limite|INTEGER|0||0
			sqlite>
Lembra de eu tirar isso depois
"""

            columns = self.cursor.fetchall()
            for column in columns:
                column_item = QTreeWidgetItem(
                    [column[1], column[2], f'"{column[1]}" {column[2]}']
                )
                table_item.addChild(column_item)
        pass


    def comboBoxTableChanged(self, index):
        if self.cursor is None or self.con is None:
            print("sem conexão ou sem cursor")
            return

        self.cursor.execute(f'SELECT * FROM {index}')
        self.col_names = [description[0] for description in self.cursor.description]
        self.rows = self.cursor.fetchall()
    
        self.update_table()

    def update_table(self):
        start_row = self.current_page * self.itemPorPage
        end_row = start_row + self.itemPorPage
        page_data = self.rows[start_row:end_row]
    
        self.tableWidget_2.setRowCount(len(page_data))
        self.tableWidget_2.setColumnCount(len(self.col_names))
        self.tableWidget_2.setHorizontalHeaderLabels(self.col_names)
    
        for row_num, row_data in enumerate(page_data):
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget_2.setItem(row_num, col_num, item)
    
        self.tableWidget_2.resizeColumnsToContents()


    #def comboBoxTableChanged(self, index):
        #if self.cursor is None or self.con is None:
        #    print("sem conexão ou sem cursor")
        #    return

        #self.cursor.execute(f'SELECT * FROM {index}')
        #col_names = [description[0] for description in self.cursor.description]
        #rows = self.cursor.fetchall()
        
        #self.tableWidget_2.setRowCount(len(rows))
        #self.tableWidget_2.setColumnCount(len(col_names))
        #self.tableWidget_2.setHorizontalHeaderLabels(col_names)
        
        #for row_num, row_data in enumerate(rows):
        #    for col_num, data in enumerate(row_data):
        #        item = QTableWidgetItem(str(data))
        #        self.tableWidget_2.setItem(row_num, col_num, item)
        #
        #self.tableWidget_2.resizeColumnsToContents()
        #print(index)

    def open_sql(self):
        print('aa')
        self.comboBox.clear()
        db_path = QFileDialog.getOpenFileNames(self,"Selecione um","/home","Sqlite (*.db *.sql *.sqlite3 *.sqlite)")
        db_path = db_path[0][0]
        
        self.con, self.cursor = open_database(db_path)  # Use a função do utils
        
        tables = list_tables(self.cursor)  # Use a função do utils
        self.comboBox.addItems(tables)
        self.comboBox.setEnabled(True)

        self.SQLStructure() # Iniciar estrutura da tabela do banco 


    def new_sql(self):
        self.nova_janela = NewDbWindow()
        self.nova_janela.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Sqliteui()
    window.show()
    sys.exit(app.exec())
