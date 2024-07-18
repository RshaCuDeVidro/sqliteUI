#ifndef SQLITEUI_H
#define SQLITEUI_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class SQLiteUi;
}
QT_END_NAMESPACE

class SQLiteUi : public QMainWindow
{
    Q_OBJECT

public:
    SQLiteUi(QWidget *parent = nullptr);
    ~SQLiteUi();

private:
    Ui::SQLiteUi *ui;
};
#endif // SQLITEUI_H
