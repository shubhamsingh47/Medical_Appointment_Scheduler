import mysql.connector as connection
from config import AppConfig


def create_connection(database=None):
    if database:
        conn = connection.connect(
            host=AppConfig.DB_HOST,
            user=AppConfig.DB_USER,
            password=AppConfig.DB_PASSWORD,
            database=database,
            use_pure=True
        )
    else:
        conn = connection.connect(
            host=AppConfig.DB_HOST,
            user=AppConfig.DB_USER,
            password=AppConfig.DB_PASSWORD,
            use_pure=True
        )
    return conn


def create_database():
    conn = create_connection()
    c = conn.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS Medical_Scheduler")
    conn.commit()
    conn.close()
