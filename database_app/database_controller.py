import sqlite3
from tools import sqlite3_code_generator


class DatabaseController:
    def __init__(self, database_name, table_name, table_structure):
        self.database_name = database_name
        self.table_name = table_name
        self.table_structure = table_structure

        self.create_table_sqlite3_code = \
            sqlite3_code_generator.create_table_string(self.table_name, self.table_structure)
        self.drop_table_sqlite3_code = \
            sqlite3_code_generator.drop_table

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
        print(f"table {self.table_name} created")

    def drop_table(self, table_name):
        conn, c = self._open_db_connection(self.database_name)
        custom_table_code = self.drop_table_sqlite3_code + table_name
        c.execute(custom_table_code)
        self._commit_and_close_db_connection(conn)
        print(f"table {self.table_name} deleted")
