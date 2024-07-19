# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_db.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Tabela(object):
    def setupUi(self, Tabela):
        if not Tabela.objectName():
            Tabela.setObjectName(u"Tabela")
        Tabela.resize(800, 600)
        self.verticalLayout_2 = QVBoxLayout(Tabela)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nome_tabela = QLineEdit(Tabela)
        self.nome_tabela.setObjectName(u"nome_tabela")

        self.verticalLayout_2.addWidget(self.nome_tabela)

        self.tabWidget = QTabWidget(Tabela)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adicionar_campo = QPushButton(self.tab)
        self.adicionar_campo.setObjectName(u"adicionar_campo")

        self.horizontalLayout.addWidget(self.adicionar_campo)

        self.remover_campo = QPushButton(self.tab)
        self.remover_campo.setObjectName(u"remover_campo")

        self.horizontalLayout.addWidget(self.remover_campo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabela_campos = QTableWidget(self.tab)
        if (self.tabela_campos.columnCount() < 3):
            self.tabela_campos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_campos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_campos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_campos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabela_campos.setObjectName(u"tabela_campos")

        self.verticalLayout.addWidget(self.tabela_campos)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.adicionar_res = QPushButton(self.tab_2)
        self.adicionar_res.setObjectName(u"adicionar_res")

        self.horizontalLayout_2.addWidget(self.adicionar_res)

        self.remover_rest = QPushButton(self.tab_2)
        self.remover_rest.setObjectName(u"remover_rest")

        self.horizontalLayout_2.addWidget(self.remover_rest)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabela_rest = QTableWidget(self.tab_2)
        if (self.tabela_rest.columnCount() < 4):
            self.tabela_rest.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_rest.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_rest.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_rest.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_rest.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tabela_rest.setObjectName(u"tabela_rest")

        self.verticalLayout_3.addWidget(self.tabela_rest)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.texto_sql = QPlainTextEdit(Tabela)
        self.texto_sql.setObjectName(u"texto_sql")
        self.texto_sql.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.texto_sql)


        self.retranslateUi(Tabela)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Tabela)
    # setupUi

    def retranslateUi(self, Tabela):
        Tabela.setWindowTitle(QCoreApplication.translate("Tabela", u"Tabela", None))
        self.nome_tabela.setInputMask("")
        self.nome_tabela.setPlaceholderText(QCoreApplication.translate("Tabela", u"Nome da tabela", None))
        self.adicionar_campo.setText(QCoreApplication.translate("Tabela", u"Adicionar", None))
        self.remover_campo.setText(QCoreApplication.translate("Tabela", u"Remover", None))
        ___qtablewidgetitem = self.tabela_campos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Tabela", u"Nome", None));
        ___qtablewidgetitem1 = self.tabela_campos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Tabela", u"Tipo", None));
        ___qtablewidgetitem2 = self.tabela_campos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Tabela", u"PK", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Tabela", u"Campos", None))
        self.adicionar_res.setText(QCoreApplication.translate("Tabela", u"Adicionar", None))
        self.remover_rest.setText(QCoreApplication.translate("Tabela", u"Remover", None))
        ___qtablewidgetitem3 = self.tabela_rest.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Tabela", u"Colunas", None));
        ___qtablewidgetitem4 = self.tabela_rest.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Tabela", u"Tipo", None));
        ___qtablewidgetitem5 = self.tabela_rest.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Tabela", u"Nome", None));
        ___qtablewidgetitem6 = self.tabela_rest.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Tabela", u"SQL", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Tabela", u"Restri\u00e7\u00f5es", None))
    # retranslateUi

