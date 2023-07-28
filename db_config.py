import psycopg2
from psycopg2 import sql

# Replace the values with your actual DB values
DATABASE_CONFIG = {
    'host': 'localhost',
    'dbname': 'your_database_name',
    'user': 'your_database_user',
    'password': 'your_database_password',
    'port': '5432',  # default postgres port
}

def get_db():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn
