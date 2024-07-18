#include "sqliteui.h"
#include "./ui_sqliteui.h"

SQLiteUi::SQLiteUi(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::SQLiteUi)
{
    ui->setupUi(this);
}

SQLiteUi::~SQLiteUi()
{
    delete ui;
}
