from PySide6 import QtWidgets
from resources.ui.ui_new_db import Ui_Tabela
from PySide6.QtWidgets import QTableWidgetItem, QComboBox, QCheckBox

class NewDbWindow(QtWidgets.QWidget, Ui_Tabela):
    def __init__(self):
        super(NewDbWindow, self).__init__()
        self.setupUi(self)

        self.values = []  # lista para armazenar os dados dos campos

        # Conexões
        self.nome_tabela.editingFinished.connect(self.set_table_name)
        self.adicionar_campo.clicked.connect(self.add_camp)
        self.tabela_campos.itemChanged.connect(self.handle_item_changed)

    def write_sql_text(self):
        currentText = self.texto_sql.toPlainText()
        currentText = currentText.split("\n")
        
        new_text = [currentText[0], '', currentText[-1]]
        for v in self.values:
            new_text[1] += f'   "{v["nome"]}"   {v["tipo"]}{"   PRIMARY KEY," if v["pk"] else ","}\n'

        self.texto_sql.setPlainText("\n".join(new_text))

    def set_table_name(self):
        self.texto_sql.setPlainText(f'CREATE TABLE "{self.nome_tabela.text()}" (\n\n)')
        self.adicionar_campo.setEnabled(True)
        self.remover_campo.setEnabled(True)

    def add_camp(self):
        currentIndex = self.tabela_campos.rowCount()
        self.tabela_campos.insertRow(currentIndex)

        tipo = QComboBox()
        tipo.addItems(["INTEGER", "TEXT", "NUMERIC", "BLOB"])

        pk = QCheckBox()

        # cria e configura os widgets da tabela
        self.tabela_campos.setItem(currentIndex, 0, QTableWidgetItem(f"Field{currentIndex+1}"))
        self.tabela_campos.setCellWidget(currentIndex, 1, tipo)  # tipo de variável
        self.tabela_campos.setCellWidget(currentIndex, 2, pk)  # se é pk

        # adicionar a linha ao dicionário de valores
        self.values.append({
            "nome": f"Field{currentIndex + 1}",
            "tipo": tipo.currentText(),
            "pk": pk.isChecked()
        })

        # conectar os sinais dos widgets pra alterar o sql_text
        tipo.currentIndexChanged.connect(lambda index: self.update_value(currentIndex, "tipo", tipo.currentText()))
        pk.toggled.connect(lambda checked: self.update_value(currentIndex, "pk", checked))

        self.write_sql_text()  # atualizar o texto SQL com os valores

    def handle_item_changed(self, item):
        row = item.row()
        col = item.column()

        if col == 0:  # se a coluna alterada for a coluna de nome
            self.update_value(row, "nome", item.text())

    def update_value(self, row, key, value):
        if 0 <= row < len(self.values):
            self.values[row][key] = value
            self.write_sql_text()
