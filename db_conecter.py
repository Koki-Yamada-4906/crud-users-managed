import mysql.connector as mydb


def conn_db():
    '''
    データベースに接続するためのコネクションを作成
    '''
    conn = mydb.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Nero8910',
        database='mydb'
    )
    return conn


