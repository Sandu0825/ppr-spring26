import psycopg2
from config import DB_CONFIG


#function to connect to PostgreSQL database
def connect():
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            dbname=DB_CONFIG["dbname"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"]
        )
        return conn

    except Exception as e:
        print("Connection error:", e)
        return None