from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    async def get(self, **kwargs) -> dict: ...

    @abstractmethod
    async def create(self, **kwargs) -> dict: ...

    @abstractmethod
    async def update(self, **kwargs) -> dict: ...

    @abstractmethod
    async def delete(self, **kwargs) -> dict: ...

    @abstractmethod
    async def filter(self, **kwargs) -> [dict]: ...

    async def paginate(self, items, page=0, limit=10) -> list:
        start = page * limit
        end = start + limit
        return items[start:end]

    async def sort(self, key='rating', reverse=True) -> list:
        return sorted(self.data, key=lambda x: float(x.get(key, 0)), reverse=reverse)

    async def _compare_kwargs(self, data: dict, **kwargs) -> bool:
        for key, value in kwargs.items():
            if data.get(key) != value:
                return False

        return True