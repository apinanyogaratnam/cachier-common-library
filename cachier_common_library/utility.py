import sqlite3

import pandas as pd


def get_sqlite_connection(filename: str) -> sqlite3.Connection:
    connection: sqlite3.Connection = sqlite3.connect(filename)
    return connection


def query_sqlite_database(connection: sqlite3.Connection, query: str) -> object:
    table: pd.DataFrame = pd.read_sql_query(query, connection)
    return table


def write_sqlite_database(connection: sqlite3.Connection, query: str) -> bool:
    cursor = connection.cursor()
    is_successful = False

    try:
        cursor.execute(query)
        connection.commit()
        is_successful = True
    except Exception as error:
        print(error)
        connection.rollback()

    cursor.close()

    return is_successful

# TODO: create write_sqlite_database_with_parameters() function
