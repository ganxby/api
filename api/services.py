import psycopg2
import json

from datetime import datetime
from psycopg2 import errors


def database_handler(*args):
    f = open('config.json', 'r')
    parsed_file = json.load(f)

    conn = psycopg2.connect(dbname=parsed_file['dbname'], user=parsed_file['user'],
                            password=parsed_file['password'], host=parsed_file['host'],
                            port=parsed_file['port'])
    conn.autocommit = True

    cursor = conn.cursor()

    try:
        cursor.execute(args[0], args[1])

    except psycopg2.errors.lookup("42P01"):
        print('INFO:     [ Table not found ]')

    except psycopg2.ProgrammingError as err:
        print(f'INFO:     [ {err} ]')

    finally:
        cursor.close()
        conn.close()


def save_data(uid, url):
    database_handler(
        """INSERT INTO redirect_data (uid, url, ctime) VALUES (%(uid)s, %(url)s, %(timestamp)s);""",
        {'uid': uid, 'url': url, 'timestamp': datetime.now()}
    )

    print('INFO:     [ Save redirect data ]')
