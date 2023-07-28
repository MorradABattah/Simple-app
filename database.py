import psycopg2
from psycopg2 import OperationalError

def create_conn():
    conn = None
    try:
        conn = psycopg2.connect(
            database="jenkins",
            user="jenkins",
            password="jenkinspassword",
            host="3.135.188.206", # Update with your PostgreSQL server IP if not localhost
            port="5432",
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return conn

connection = create_conn()