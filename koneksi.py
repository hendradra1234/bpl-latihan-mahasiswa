from mysql.connector import *
import config

def buka_koneksi():
    db = None
    host = config.host
    port = config.port
    user = config.username
    password = config.password
    database = config.database
    try:
        db = connect(host = host, port = port, user=user, password = password, database = database)
    except DatabaseError as e:
        print(f'Koneksi Gagal: {e}')
    return db