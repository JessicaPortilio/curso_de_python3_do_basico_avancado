import sqlite3

from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# CUIDADO: fazendo delete sem where
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name ={TABLE_NAME}'
# )
# connection.commit()

# Registrar valores nas colunas da tabela
# cursor.execute(
#     f'INSERT INTO {TABLE_NAME} (id, name, weight) '
#     'VALUES (NULL, "Jessica", 62.300)'
#     )
# connection.commit()

# sql = (
#     f'INSERT INTO {TABLE_NAME}'
#     '(name, weight)'
#     'VALUES'
#     '(?,?)'
# )

# cursor.execute(sql, ['Joana', 52.500])
# connection.commit()

# cursor.executemany(sql, [['Maria', 58.200], ['Pedtro', 98]])
# connection.commit()


sql = (
    f'INSERT INTO {TABLE_NAME}'
    '(name, weight)'
    'VALUES'
    '(:name,:weight)'
)

cursor.executemany(sql, (
    {'name': 'Paulo', 'weight' : 43.500},
    {'name': 'Vanessa', 'weight' : 72.500},
    {'name': 'Thiago', 'weight' : 65.500}
))
connection.commit()



if __name__ =='__main__':
    print(sql)
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    # fetchall todos os valores fetchone um primeiro registro
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.execute(
       f'DELETE FROM {TABLE_NAME} ' 
       'WHERE id="9"'
    )
    connection.commit()

    cursor.execute(
       f'UPDATE {TABLE_NAME} '
       'SET name ="QUALQUER", weight= 67.32 ' 
       'WHERE id="2"'
    )
    connection.commit()
    
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

   

   

    cursor.close()
    connection.close()
