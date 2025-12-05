import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

def get_db_url():
    POSTGRES_USERNAME = os.environ["POSTGRES_USERNAME"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_SERVER = os.environ["POSTGRES_SERVER"]
    POSTGRES_DATABASE = os.environ["POSTGRES_DATABASE"]

    DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DATABASE}"

    return DATABASE_URL




def test_postgress_connection(connection_string):
    try:
        conn = psycopg2.connect(connection_string)

        cur = conn.cursor()

        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print("Connetion successful!")
        print(f"PostgresSQL version: {db_version}")

        cur.close()
        conn.close()
        print("Connection closed")
        return True
    except Exception as e:
        print("Connection failed")
        print(e)
        return False

DATABASE_URL = get_db_url()

test_postgress_connection(DATABASE_URL)