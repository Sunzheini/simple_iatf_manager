import sqlite3
from tools import sqlite3_code


class DatabaseController:
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

        self.create_table_sqlite3_code = \
            sqlite3_code.create_table.replace('processes', self.table_name)
        self.drop_table_sqlite3_code = \
            sqlite3_code.drop_table

    @staticmethod
    def _open_db_connection(database_name):
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        return conn, c

    @staticmethod
    def _commit_and_close_db_connection(conn):
        conn.commit()
        conn.close()

    def create_database_and_table(self):
        conn, c = self._open_db_connection(self.database_name)
        c.execute(self.create_table_sqlite3_code)
        self._commit_and_close_db_connection(conn)

    def drop_table(self, table_name):
        conn, c = self._open_db_connection(self.database_name)
        custom_table_code = self.drop_table_sqlite3_code.replace('processes', table_name)
        c.execute(custom_table_code)
        self._commit_and_close_db_connection(conn)
