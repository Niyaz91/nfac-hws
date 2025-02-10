from .base_repository import BaseRepository
import json
class JSONRepository(BaseRepository):
    def __init__(self, path: str):
        with open(path, 'r') as file:
            self.data = json.load(file)

    async def get(self, **kwargs) -> dict | None:
        for item in self.data:
            if await self._compare_kwargs(item, **kwargs):
                return item
        return None

    async def create(self, **kwargs) -> dict:...
    async def update(self, **kwargs) -> dict:...
    async def delete(self, **kwargs) -> dict:...

    async def filter(self, **kwargs) -> list[dict]:
        result = []
        for item in self.data:
            if await self._compare_kwargs(item, **kwargs):
                result.append(item)
        return result