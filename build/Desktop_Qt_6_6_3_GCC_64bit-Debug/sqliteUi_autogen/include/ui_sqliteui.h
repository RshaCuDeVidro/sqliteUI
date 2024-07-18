/********************************************************************************
** Form generated from reading UI file 'sqliteui.ui'
**
** Created by: Qt User Interface Compiler version 6.6.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SQLITEUI_H
#define UI_SQLITEUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SQLiteUi
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton_open;
    QPushButton *pushButton_2_new;
    QSpacerItem *horizontalSpacer;
    QTabWidget *tabWidget_paginas;
    QWidget *tab;
    QHBoxLayout *horizontalLayout_3;
    QTreeWidget *treeWidget;
    QWidget *Navegar;
    QHBoxLayout *horizontalLayout_2;
    QTableWidget *tableWidget_2;
    QWidget *tab_3;
    QVBoxLayout *verticalLayout_2;
    QTextEdit *textEdit;
    QTableWidget *tableWidget;

    void setupUi(QMainWindow *SQLiteUi)
    {
        if (SQLiteUi->objectName().isEmpty())
            SQLiteUi->setObjectName("SQLiteUi");
        SQLiteUi->resize(809, 448);
        centralwidget = new QWidget(SQLiteUi);
        centralwidget->setObjectName("centralwidget");
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName("verticalLayout");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        pushButton_open = new QPushButton(centralwidget);
        pushButton_open->setObjectName("pushButton_open");
        pushButton_open->setMinimumSize(QSize(150, 30));
        pushButton_open->setStyleSheet(QString::fromUtf8("/* Estilo inicial do bot\303\243o */\n"
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
""));

        horizontalLayout->addWidget(pushButton_open);

        pushButton_2_new = new QPushButton(centralwidget);
        pushButton_2_new->setObjectName("pushButton_2_new");
        pushButton_2_new->setMinimumSize(QSize(150, 30));
        pushButton_2_new->setStyleSheet(QString::fromUtf8("/* Estilo inicial do bot\303\243o */\n"
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
""));

        horizontalLayout->addWidget(pushButton_2_new);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Policy::Expanding, QSizePolicy::Policy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);


        verticalLayout->addLayout(horizontalLayout);

        tabWidget_paginas = new QTabWidget(centralwidget);
        tabWidget_paginas->setObjectName("tabWidget_paginas");
        tab = new QWidget();
        tab->setObjectName("tab");
        horizontalLayout_3 = new QHBoxLayout(tab);
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        treeWidget = new QTreeWidget(tab);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setText(0, QString::fromUtf8("1"));
        treeWidget->setHeaderItem(__qtreewidgetitem);
        treeWidget->setObjectName("treeWidget");

        horizontalLayout_3->addWidget(treeWidget);

        tabWidget_paginas->addTab(tab, QString());
        Navegar = new QWidget();
        Navegar->setObjectName("Navegar");
        horizontalLayout_2 = new QHBoxLayout(Navegar);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        tableWidget_2 = new QTableWidget(Navegar);
        tableWidget_2->setObjectName("tableWidget_2");

        horizontalLayout_2->addWidget(tableWidget_2);

        tabWidget_paginas->addTab(Navegar, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName("tab_3");
        verticalLayout_2 = new QVBoxLayout(tab_3);
        verticalLayout_2->setObjectName("verticalLayout_2");
        textEdit = new QTextEdit(tab_3);
        textEdit->setObjectName("textEdit");

        verticalLayout_2->addWidget(textEdit);

        tableWidget = new QTableWidget(tab_3);
        tableWidget->setObjectName("tableWidget");

        verticalLayout_2->addWidget(tableWidget);

        tabWidget_paginas->addTab(tab_3, QString());

        verticalLayout->addWidget(tabWidget_paginas);

        SQLiteUi->setCentralWidget(centralwidget);

        retranslateUi(SQLiteUi);

        tabWidget_paginas->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(SQLiteUi);
    } // setupUi

    void retranslateUi(QMainWindow *SQLiteUi)
    {
        SQLiteUi->setWindowTitle(QCoreApplication::translate("SQLiteUi", "SQLiteUi", nullptr));
        pushButton_open->setText(QCoreApplication::translate("SQLiteUi", "Abrir Banco de Dados", nullptr));
        pushButton_2_new->setText(QCoreApplication::translate("SQLiteUi", "Novo Banco de Dados", nullptr));
        tabWidget_paginas->setTabText(tabWidget_paginas->indexOf(tab), QCoreApplication::translate("SQLiteUi", "Estrutura do Banco", nullptr));
        tabWidget_paginas->setTabText(tabWidget_paginas->indexOf(Navegar), QCoreApplication::translate("SQLiteUi", "Navegar pelo Banco", nullptr));
        tabWidget_paginas->setTabText(tabWidget_paginas->indexOf(tab_3), QCoreApplication::translate("SQLiteUi", "Executar SQL", nullptr));
    } // retranslateUi

};

namespace Ui {
    class SQLiteUi: public Ui_SQLiteUi {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SQLITEUI_H
