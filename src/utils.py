import sqlite3

def list_tables(cur):
    lista = []
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    busca = cur.fetchall()
    
    for item in busca:
        lista.append(item[0])
    
    return lista

def open_database(db_path):
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    return con, cursor
