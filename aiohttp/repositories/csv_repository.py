from .base_repository import BaseRepository
import csv

class CSVRepository(BaseRepository):
    def __init__(self, path: str):
        self.path = path

    def _read_csv(self):
        with open(self.path, 'r') as file:
            return list(csv.DictReader(file))

    def get(self) -> [dict]:
        return self._read_csv()


    async def create(self, **kwargs) -> dict: ...
    async def update(self, **kwargs) -> dict: ...
    async def delete(self, **kwargs) -> dict: ...

    def filter(self, **kwargs) -> [dict]:
        data_list = self._read_csv()
        res = []
        for row in data_list:
            matches = True
            for key, value in kwargs.items():
                if row.get(key) != value:
                    matches = False
                    break
            if matches:
                res.append(row)
        return res
