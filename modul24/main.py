import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees

    id Integer primary key autoincrement,
    name text not null,
    position text not null,
    departament text not null
    
    ''')