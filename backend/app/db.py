import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "mysql-service"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", "password"),
        database=os.environ.get("MYSQL_DATABASE", "productdb")
    )
