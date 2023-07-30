import psycopg2
from psycopg2 import sql

# Replace the values with your actual DB values
DATABASE_CONFIG = {
    'host': '3.141.10.82',
    'dbname': 'jenkins',
    'user': 'jenkins',
    'password': 'jenkins',
    'port': '5432',  # default postgres port
}

def get_db():
    conn = psycopg2.connect(**DATABASE_CONFIG)
    return conn
