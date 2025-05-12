import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="jobs_db"
    )
