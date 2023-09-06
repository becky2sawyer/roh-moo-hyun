import sqlite3
import os


class ConnectionManager:

    def __init__(self, database_file="init.db"):
        data_path = os.path.join(os.path.dirname(__file__), database_file)
        # print(data_path.center(100, "*"))
        self.database_file = data_path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.database_file, isolation_level=None)

    def get_connection(self):
        if not self.connection:
            self.connect()

        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()

            self.connection = None
