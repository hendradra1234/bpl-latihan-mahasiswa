from mysql.connector import *

def buka_koneksi():
    db = None
    host = 'localhost'
    port = 3306
    user = 'root'
    password = ''
    database = 'bpl_0525'
    try:
        db = connect(host = host, port = port, user=user, password = password, database = database)
    except DatabaseError as e:
        print(f'Koneksi Gagal: {e}')
    return db