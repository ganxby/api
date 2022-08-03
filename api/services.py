import psycopg2

from datetime import datetime
from psycopg2 import errors


def database_handler(*args):
    conn = psycopg2.connect(dbname='simple_api', user='postgres',
                            password='admin', host='172.24.0.10',
                            port=5432)
    conn.autocommit = True

    cursor = conn.cursor()

    try:
        cursor.execute(args[0])

    except psycopg2.errors.lookup("42P01"):
        return 'Table not found'

    except psycopg2.ProgrammingError as err:
        return err

    finally:
        cursor.close()
        conn.close()


def save_data(uid, url):
    database_handler(
        f'INSERT INTO redirect_data (uid, url, ctime) '
        f"VALUES ('{uid}', '{url}', '{datetime.now()}');"
    )

    return 1
