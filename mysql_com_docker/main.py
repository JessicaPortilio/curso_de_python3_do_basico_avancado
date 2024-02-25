# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import pymysql.cursors
import dotenv
import os
dotenv.load_dotenv()

TABLE_NAME = 'CUSTOMERS'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    cursorclass= pymysql.cursors.DictCursor,
    # cursorclass=pymysql.cursors.SSDictCursor,
)

print(os.environ['MYSQL_DATABASE'])
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            ' idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # CUIDADO ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        cursor.execute(sql, ('Roberto', 30))
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data = {
            "name": "Jessica",
            "age": 30
        }
        cursor.execute(sql, data)
        print(sql)
        print(data)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = (
            {"name": "Juliana", "age": 54},
            {"name": "Paulo", "age": 43},
            {"name": "João", "age": 34},
        )
        result = cursor.executemany(sql, data2)
        print(sql)
        print(data2)
        print(result)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data3 = (
            ("Cleison", 14),
            ("Sarah", 33),
            ("Kelly", 65),
        )
        result = cursor.executemany(sql, data3)
        print(sql)
        print(data3)
        print(result)
    connection.commit()

# Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # id = input('Informa o id: ')
        id = 5
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id > %s'
        )
        
        cursor.execute(sql, (id))

        # print(cursor.mogrify(sql, id))
        data5 = cursor.fetchall()
        for row in data5:
            _id, nome, idade = row
            print(_id, nome, idade)   

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
       
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE ID = 3'
            
        )
        cursor.execute(sql)
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()
        
        for row in data6:
           print(row)
    
    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
       
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = "Paula", idade = 25 '
            'WHERE ID = 4'
            
        )
        cursor.execute(sql)
        

        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()
        for row in data6:
            print(row)
        
        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)
        print('rownumber', cursor.rownumber)
        cursor.execute(
            f'SELECT id FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1 '
        )
        lastIdFromSelect = cursor.fetchone()

        print('lastrowid na mão', lastIdFromSelect)

        # # data6 = cursor.fetchall()
        # for row in cursor.fetchall():
        #     print(row)

        # print('---------------------------------')
        # cursor.scroll(-2)
        # cursor.scroll(1, 'absolute')
        
        # for row in cursor.fetchall():
        #     print(row)

        # SSDictCursor
                
        # for row in cursor.fetchall_unbuffered():
        #    print(row)

        #    if row['id'] == 5:
        #        break

        # print('---------------------------------')
        # for row in cursor.fetchall_unbuffered():
        #    print(row)
    connection.commit()

