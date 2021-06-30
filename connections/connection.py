import mysql.connector

def new_connection(db):
    db = mysql.connector.connect(
        host="localhost",
        user="adonais1_admin",
        password="Adonai1816",
        database=db
    )
    return db