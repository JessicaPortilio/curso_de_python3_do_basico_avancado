import sqlite3
from primeiro_arquivo_sqlite import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
# fetchall todos os valores fetchone um primeiro registro
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
connection.close()

# CRUD
# CREATE - INSERT
# READ - LER - SELECT
# UPDADE - AUTUALIZAR
# DELETE - DELETAR

# C (Create): Criar ou inserir novos dados no sistema.
# R (Read): Ler ou recuperar dados existentes do sistema.
# U (Update): Atualizar ou modificar dados existentes no sistema.
# D (Delete): Deletar ou remover dados existentes do sistema.
# CRUD - CREATE  READ   UPDATE  DELETE
# SQL - INSERT  SELECT  UPDATE  DELETE