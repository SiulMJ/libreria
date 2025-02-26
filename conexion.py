import mysql.connector

def con():
    conection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='libreria'
        )

    return conection
