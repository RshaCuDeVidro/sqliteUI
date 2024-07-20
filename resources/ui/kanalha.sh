uic -g python ./sqliteui.ui -o ui_sqliteui.py
sed -i 's/PySide2/PySide6/g' ./ui_sqliteui.py

