import sqlite3


class ConnectionManager:

    def __init__(self, database_file="init.db"):
        self.database_file = database_file
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
