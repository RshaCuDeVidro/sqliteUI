#include "sqliteui.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SQLiteUi w;
    w.show();
    return a.exec();
}
