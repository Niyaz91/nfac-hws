import asyncpg

from base_repository import BaseRepository

class SQLRepository(BaseRepository):
    def __init__(self, table_name):
        self.table_name = table_name

    async get_connection(self):
