from resources.ui.fodase import Ui_SQLiteUi
from PySide6 import QtWidgets, QtCore, QtGui
import sys
import sqlite3
from PySide6.QtWidgets import QFileDialog, QTableWidgetItem
                                           
class Sqliteui(QtWidgets.QMainWindow, Ui_SQLiteUi):
    def __init__(self):
        super(Sqliteui, self).__init__()
        self.setupUi(self)
        self.pushButton_open.clicked.connect(self.open_sql)


    def open_sql(self):
        print('aa')
        db_path = QFileDialog.getOpenFileNames(self,"Selecione um","/home","Sqlite (*.db *.sql)")
        db_path = db_path[0][0]
        
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Exemplo de consulta para pegar o nome das colunas
        cursor.execute('SELECT * FROM users_use')
        col_names = [description[0] for description in cursor.description]

        # Exemplo de consulta para pegar os dados
        cursor.execute('SELECT * FROM users_use')
        rows = cursor.fetchall()

        # Fechando conexão
        connection.close()

        # Configurando a tabela no widget
        self.tableWidget_2.setRowCount(len(rows))
        self.tableWidget_2.setColumnCount(len(col_names))

        # Definindo os nomes das colunas
        self.tableWidget_2.setHorizontalHeaderLabels(col_names)

        # Inserindo os dados na tabela
        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget_2.setItem(row_num, col_num, item)

        # Ajustando o tamanho das colunas para o conteúdo
        self.tableWidget_2.resizeColumnsToContents()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Sqliteui()
    window.show()
    sys.exit(app.exec())
