import json
import sqlite3

from datetime import datetime, timedelta

from utility import get_sqlite_connection, query_sqlite_database, write_sqlite_database


class SqliteDriver:
    def __init__(self: 'SqliteDriver', filename: str) -> None:
        self.filename = filename

    def read_data(self: 'SqliteDriver', key: str) -> object | None:
        if not key: return None

        with get_sqlite_connection(self.filename) as connection:
            query = f'''
                SELECT cache_value, DATETIME(cache_expiry) AS cache_expiry
                FROM cache
                WHERE cache_key = '{key}';
            '''

            result = query_sqlite_database(connection, query).to_dict('records')

            if not result: return None

            cache_expired = datetime.utcnow() > datetime.strptime(result[0]['cache_expiry'], '%Y-%m-%d %H:%M:%S')

            if cache_expired:
                self.delete_data(key, connection)
                return None

        return json.loads(result[0]['cache_value'])

    def write_data(self: 'SqliteDriver', key: str, value: str, expiry: int | None = None) -> bool:
        if not key: return False

        # deserializing the value
        value = json.dumps(value)

        if not expiry:
            expiry = 'NULL'
        else:
            expiry_date = datetime.utcnow() + timedelta(seconds=expiry)
            encoded_expiry = expiry_date.isoformat()

        with get_sqlite_connection(self.filename) as connection:
            # check if key already exists in database
            query = f'''
                SELECT COUNT(*) AS count
                FROM cache
                WHERE cache_key = '{key}';
            '''

            result = query_sqlite_database(connection, query).to_dict('records')

            is_key_exists = result[0]['count'] > 0
            if is_key_exists:
                # update data
                update_data_query = f'''
                    UPDATE cache
                    SET
                        cache_value = '{value}',
                        cache_expiry = '{encoded_expiry}'
                    WHERE cache_key = '{key}';
                '''

                return write_sqlite_database(connection, update_data_query)

            # insert data if key does not exist
            insert_data_query = f'''
                INSERT INTO cache (cache_key, cache_value, cache_expiry)
                VALUES ('{key}', '{value}', '{encoded_expiry}');
            '''

            return write_sqlite_database(connection, insert_data_query)

    def delete_data(self: 'SqliteDriver', key: str, connection: sqlite3.Connection) -> bool:
        delete_data_query = f'''
            DELETE FROM cache
            WHERE cache_key = '{key}';
        '''

        return write_sqlite_database(connection, delete_data_query)
