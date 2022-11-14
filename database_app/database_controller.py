import sqlite3
from tools import sqlite3_code_generator


class DatabaseController:
    def __init__(self, database_name):
        self.database_name = database_name

    @staticmethod
    def _open_db_connection(database_name):
        conn = sqlite3.connect(database_name)
        c = conn.cursor()
        return conn, c

    @staticmethod
    def _commit_and_close_db_connection(conn):
        conn.commit()
        conn.close()

    def create_database_and_table(self, table_name, table_structure):
        create_table_sqlite3_code = \
            sqlite3_code_generator.create_table_string(table_name, table_structure)
        conn, c = self._open_db_connection(self.database_name)
        c.execute(create_table_sqlite3_code)
        self._commit_and_close_db_connection(conn)
        print(f"table {table_name} created")
        return f"table {table_name} created"

    def drop_table(self, table_name):
        drop_table_sqlite3_code = sqlite3_code_generator.drop_table
        conn, c = self._open_db_connection(self.database_name)
        custom_table_code = drop_table_sqlite3_code + table_name
        try:
            c.execute(custom_table_code)
            self._commit_and_close_db_connection(conn)
            print(f"table {table_name} deleted")
            return f"table {table_name} deleted"
        except sqlite3.OperationalError:
            print("Invalid database name")
            return "Invalid database name"



