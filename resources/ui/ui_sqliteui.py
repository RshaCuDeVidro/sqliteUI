# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sqliteui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.14
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SQLiteUi(object):
    def setupUi(self, SQLiteUi):
        if not SQLiteUi.objectName():
            SQLiteUi.setObjectName(u"SQLiteUi")
        SQLiteUi.resize(809, 448)
        self.centralwidget = QWidget(SQLiteUi)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setMinimumSize(QSize(150, 30))
        self.pushButton_open.setStyleSheet(u"/* Estilo inicial do bot\u00e3o */\n"
"QPushButton {\n"
"  border: none; /* Sem borda inicialmente */\n"
"}\n"
"\n"
"/* Quando passa o mouse por cima */\n"
"QPushButton:hover {\n"
"  border: 1px solid gray; /* Borda preta */\n"
"background-color: rgb(222, 222, 222);	\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_2_new = QPushButton(self.centralwidget)
        self.pushButton_2_new.setObjectName(u"pushButton_2_new")
        self.pushButton_2_new.setMinimumSize(QSize(150, 30))
        self.pushButton_2_new.setStyleSheet(u"/* Estilo inicial do bot\u00e3o */\n"
"QPushButton {\n"
"  border: none; /* Sem borda inicialmente */\n"
"}\n"
"\n"
"/* Quando passa o mouse por cima */\n"
"QPushButton:hover {\n"
"  border: 1px solid gray; /* Borda preta */\n"
"background-color: rgb(222, 222, 222);	\n"
"}\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_2_new)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget_paginas = QTabWidget(self.centralwidget)
        self.tabWidget_paginas.setObjectName(u"tabWidget_paginas")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeWidget = QTreeWidget(self.tab)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout_3.addWidget(self.treeWidget)

        self.tabWidget_paginas.addTab(self.tab, "")
        self.Navegar = QWidget()
        self.Navegar.setObjectName(u"Navegar")
        self.Navegar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.Navegar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.Navegar)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.comboBox = QComboBox(self.Navegar)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tableWidget_2 = QTableWidget(self.Navegar)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_3.addWidget(self.tableWidget_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.tabWidget_paginas.addTab(self.Navegar, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_2 = QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.pushButton = QPushButton(self.tab_3)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.textEdit = QTextEdit(self.tab_3)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_2.addWidget(self.textEdit)

        self.tableWidget = QTableWidget(self.tab_3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.tabWidget_paginas.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget_paginas)

        SQLiteUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(SQLiteUi)

        self.tabWidget_paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SQLiteUi)
    # setupUi

    def retranslateUi(self, SQLiteUi):
        SQLiteUi.setWindowTitle(QCoreApplication.translate("SQLiteUi", u"SQLiteUi", None))
        self.pushButton_open.setText(QCoreApplication.translate("SQLiteUi", u"Abrir Banco de Dados", None))
        self.pushButton_2_new.setText(QCoreApplication.translate("SQLiteUi", u"Novo Banco de Dados", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("SQLiteUi", u"Esquema", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SQLiteUi", u"Tipo", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SQLiteUi", u"Nome", None));
        self.tabWidget_paginas.setTabText(self.tabWidget_paginas.indexOf(self.tab), QCoreApplication.translate("SQLiteUi", u"Estrutura do Banco", None))
        self.label.setText(QCoreApplication.translate("SQLiteUi", u"Tabela:", None))
        self.tabWidget_paginas.setTabText(self.tabWidget_paginas.indexOf(self.Navegar), QCoreApplication.translate("SQLiteUi", u"Navegar pelo Banco", None))
        self.label_2.setText(QCoreApplication.translate("SQLiteUi", u"Executar", None))
        self.pushButton.setText("")
        self.tabWidget_paginas.setTabText(self.tabWidget_paginas.indexOf(self.tab_3), QCoreApplication.translate("SQLiteUi", u"Executar SQL", None))
    # retranslateUi

